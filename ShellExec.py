import tkinter
import customtkinter as ctk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import paramiko
import json
import os
import logging
from PIL import Image

# Constants
CREDENTIALS_FILE = "credentials.json"
THEME_FILE = "C:/Users/Hxrrrsshhh/Desktop/ShellExec/themes/violet.json"
BACKGROUND_IMAGE = r"C:\Users/Hxrrrsshhh/Desktop/ShellExec/assets/abcde.jpg"
SCRIPTS_CONFIG_FILE = "scripts.json"
CUSTOM_SCRIPTS_DIR = "/home/hxrrrshhh/scripts/custom_scripts"

# Logging setup
logging.basicConfig(
    filename="shell_exec.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class SSHApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ShellExec")
        self.root.geometry("1280x720")

        # Set appearance mode and color theme
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme(THEME_FILE)

        # Initialize the SSH client
        self.ssh = None

        # Create frames
        self.login_frame = ctk.CTkFrame(self.root)
        self.main_frame = ctk.CTkFrame(self.root)

        self.create_toggle_button()
        self.create_login_page()

        # Load saved credentials
        self.load_credentials()

        # Load scripts from JSON and group them
        self.scripts = self.load_scripts()
        self.categories = self.group_scripts_by_category()

        self.create_main_page()

        # Show login frame by default
        self.login_frame.pack(fill="both", expand=True)

    def create_toggle_button(self):
        """Create the appearance mode toggle button."""
        self.toggle_button = ctk.CTkButton(
            self.root,
            text="Toggle Light/Dark Mode",
            command=self.toggle_appearance_mode,
            font=("Super Shiny", 14),
        )
        self.toggle_button.pack(side="top", anchor="ne", padx=10, pady=10)

    def toggle_appearance_mode(self):
        """Toggle between light and dark mode."""
        current_mode = ctk.get_appearance_mode()
        new_mode = "Dark" if current_mode == "Light" else "Light"
        ctk.set_appearance_mode(new_mode)

    def create_login_page(self):
        """Create the login page."""
        # Load background image
        background_image = Image.open(BACKGROUND_IMAGE)
        self.ctk_background_image = ctk.CTkImage(
            light_image=background_image,
            dark_image=background_image,
            size=(1920, 1080),
        )
        background_label = ctk.CTkLabel(
            master=self.login_frame, image=self.ctk_background_image, text=""
        )
        background_label.pack()

        # Create custom frame
        login_form_frame = ctk.CTkFrame(
            master=background_label, width=320, height=420, corner_radius=15
        )
        login_form_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Labels and Entry fields
        ctk.CTkLabel(
            master=login_form_frame, text="ShellExec", font=("a Area Stencil", 60)
        ).grid(
            row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="nsew", columnspan=2
        )

        # Hostname Label and Entry
        ctk.CTkLabel(
            master=login_form_frame, text="Hostname:", font=("Super Shiny", 30)
        ).grid(row=1, column=0, padx=(10, 5), pady=(10, 5), sticky="e")
        self.hostname_entry = ctk.CTkEntry(
            master=login_form_frame,
            width=200,
            placeholder_text="Hostname",
            font=("Party Confetti", 20),
        )
        self.hostname_entry.grid(
            row=1, column=1, padx=(0, 20), pady=(10, 5), sticky="w"
        )

        # Username Label and Entry
        ctk.CTkLabel(
            master=login_form_frame, text="Username:", font=("Super Shiny", 30)
        ).grid(row=2, column=0, padx=(10, 5), pady=(10, 5), sticky="e")
        self.username_entry = ctk.CTkEntry(
            master=login_form_frame,
            width=200,
            placeholder_text="Username",
            font=("Party Confetti", 20),
        )
        self.username_entry.grid(
            row=2, column=1, padx=(0, 20), pady=(10, 5), sticky="w"
        )

        # Password Label and Entry
        ctk.CTkLabel(
            master=login_form_frame, text="Password:", font=("Super Shiny", 30)
        ).grid(row=3, column=0, padx=(10, 5), pady=(10, 5), sticky="e")
        self.password_entry = ctk.CTkEntry(
            master=login_form_frame,
            width=200,
            placeholder_text="Password",
            show="*",
            font=("Party Confetti", 20),
        )
        self.password_entry.grid(
            row=3, column=1, padx=(0, 20), pady=(10, 5), sticky="w"
        )

        # Create login button
        login_button = ctk.CTkButton(
            master=login_form_frame,
            width=220,
            text="Login",
            command=self.login_action,
            corner_radius=6,
            font=("Super Shiny", 28),
        )
        login_button.grid(row=4, column=0, columnspan=2, pady=(20, 10))

    def save_credentials(self, hostname, username, password):
        """Save credentials to a JSON file."""
        credentials = {"hostname": hostname, "username": username, "password": password}
        with open(CREDENTIALS_FILE, "w") as file:
            json.dump(credentials, file)

    def load_credentials(self):
        """Load credentials from a JSON file."""
        if os.path.exists(CREDENTIALS_FILE):
            with open(CREDENTIALS_FILE, "r") as file:
                credentials = json.load(file)
                self.hostname_entry.insert(0, credentials.get("hostname", ""))
                self.username_entry.insert(0, credentials.get("username", ""))
                self.password_entry.insert(0, credentials.get("password", ""))

    def login_action(self):
        """Handle login."""
        hostname = self.hostname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not hostname or not username or not password:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            # Set up an SSH client
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=hostname, username=username, password=password)
            messagebox.showinfo("Success", "Login Successful!")
            logging.info(f"Successfully connected to {hostname}")

            # Save credentials after successful login
            self.save_credentials(hostname, username, password)

            # Switch to the main page
            self.login_frame.pack_forget()
            self.main_frame.pack(fill="both", expand=True)

        except paramiko.AuthenticationException:
            messagebox.showerror("Authentication Failed", "Invalid username or password.")
            logging.error(f"Authentication failed for user {username} on host {hostname}")
        except paramiko.SSHException as sshException:
            messagebox.showerror(
                "SSH Error", f"Unable to establish SSH connection: {sshException}"
            )
            logging.error(
                f"Unable to establish SSH connection to {hostname}: {sshException}"
            )
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")
            logging.error(f"Unexpected error during login: {e}")

    def load_scripts(self):
        """Load script data from the JSON file."""
        try:
            with open(SCRIPTS_CONFIG_FILE, "r") as file:
                data = json.load(file)
                scripts = data.get("scripts", [])
                # Ensure all scripts have a 'type' field
                for script in scripts:
                    if "type" not in script:
                        script["type"] = "normal"  # Default to 'normal'
                    # Load script content from file if it's a custom script
                    if script["type"] == "custom":
                        script_path = os.path.join(CUSTOM_SCRIPTS_DIR, script["path"])
                        try:
                            with open(script_path, "r") as script_file:
                                script["content"] = script_file.read()
                        except FileNotFoundError:
                            messagebox.showerror("Error", f"Script file not found: {script_path}")
                            script["content"] = ""  # Or handle the error as needed

                return scripts
        except FileNotFoundError:
            messagebox.showerror("Error", f"{SCRIPTS_CONFIG_FILE} not found.")
            logging.error(f"{SCRIPTS_CONFIG_FILE} not found.")
            return []
        except json.JSONDecodeError:
            messagebox.showerror(
                "Error", f"Invalid JSON format in {SCRIPTS_CONFIG_FILE}."
            )
            logging.error(f"Invalid JSON format in {SCRIPTS_CONFIG_FILE}.")
            return []

    def group_scripts_by_category(self):
        """Group scripts by category."""
        categories = {}
        for script in self.scripts:
            category = script["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append(script)
        return categories

    def create_main_page(self):
        """Create the main page with organized script buttons."""
        title_label = ctk.CTkLabel(
            self.main_frame, text="ShellExec", font=("a Area Stencil", 24)
        )
        title_label.pack(side="left", anchor="n", padx=10, pady=20)

        # Create a frame for categories and scripts
        main_frame = ctk.CTkFrame(self.main_frame)
        main_frame.pack(expand=True, fill="both")

        # Create a frame for categories
        category_frame = ctk.CTkFrame(main_frame)
        category_frame.pack(side="left", fill="y", padx=10)

        # Create a frame for script buttons
        self.script_frame = ctk.CTkFrame(main_frame)
        self.script_frame.pack(side="right", fill="both", expand=True)

        # Create category buttons
        for category in self.categories:
            button = ctk.CTkButton(
                category_frame,
                text=category,
                font=("Party Confetti", 16),
                command=lambda c=category: self.show_scripts(c, self.categories[c]),
            )
            button.pack(pady=5, fill="x")

        # Create a logout button at the bottom right
        logout_button = ctk.CTkButton(
            self.main_frame,
            text="Logout",
            font=("Super Shiny", 20),
            command=self.logout,
            fg_color="red",
        )
        logout_button.pack(side="bottom", anchor="se", padx=10, pady=10)

        # Create a manage script button at the bottom left
        manage_script_button = ctk.CTkButton(
            self.main_frame,
            text="Manage Scripts",
            font=("Super Shiny", 20),
            command=self.open_script_management_dialog,
            fg_color="blue",
        )
        manage_script_button.pack(side="bottom", anchor="sw", padx=10, pady=10)

        # Create a refresh button at the top right
        refresh_button = ctk.CTkButton(
            self.main_frame,
            text="Refresh",
            font=("Super Shiny", 20),
            command=self.refresh_scripts,
        )
        refresh_button.pack(side="top", anchor="ne", padx=10, pady=10)

    def refresh_scripts(self):
        """Refresh the list of scripts."""
        self.scripts = self.load_scripts()
        self.categories = self.group_scripts_by_category()
        self.show_scripts("Custom", self.categories.get("Custom", []))

    def show_scripts(self, category, scripts):
        """Display scripts for the selected category."""
        # Clear the script frame
        for widget in self.script_frame.winfo_children():
            widget.destroy()

        title_label = ctk.CTkLabel(
            self.script_frame, text=f"{category} Scripts", font=("Party Confetti", 20)
        )
        title_label.pack(pady=20)

        # Create buttons for scripts in the selected category
        for script in scripts:
            script_frame = ctk.CTkFrame(self.script_frame)
            script_frame.pack(pady=5, fill="x")

            button = ctk.CTkButton(
                script_frame,
                text=script["title"],
                font=("Party Confetti", 16),
                command=lambda s=script: self.run_script(s),
            )
            button.pack(side="left", fill="x", expand=True)

    def run_script(self, script):
        """Execute the selected script."""
        print(f"Running script: {script['title']}")  # Debugging
        parameters = script.get("parameters", [])
        print(f"Parameters: {parameters}")  # Debugging
        inputs = {}

        for param in parameters:
            print(f"Getting input for parameter: {param['name']}")  # Debugging
            user_input = self.get_user_input(param["prompt"])
            if not user_input:
                messagebox.showerror(
                    "Error", f"Input for '{param['name']}' is required."
                )
                logging.warning(f"User did not provide input for '{param['name']}'")
                return

            inputs[param["name"]] = user_input

        if script["type"] == "custom":
            # Execute the script content directly
            script_content = script.get("content", "")
            self.execute_command(script_content, inputs, is_custom=True)
        else:
            # Determine the correct base path
            base_path = "/home/hxrrrshhh/scripts/"
            full_script_path = os.path.join(base_path, script["path"])
            self.execute_command(full_script_path, inputs)

    def execute_command(self, command, inputs=None, is_custom=False):
        """Execute a script or command with the provided inputs."""
        if not self.ssh:
            messagebox.showerror("Error", "No SSH connection established.")
            logging.error("No SSH connection established.")
            return

        # For custom scripts, we're passing the script content as the 'command'
        if is_custom:
            # Replace placeholders in the script content with user inputs
            if inputs:
                for key, value in inputs.items():
                    command = command.replace(f"${{{key}}}", value)
            # Wrap the script content in a way that it can be executed remotely
            command = f"bash -c \"{command}\""
        else:
            if inputs:
                command = f"{command} {inputs['num1']} {inputs['num2']}"
            command = f"{command}"

        try:
            stdin, stdout, stderr = self.ssh.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            self.show_output(output, error)
            logging.info(f"Executed command: {command}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to execute command: {e}")
            logging.error(f"Failed to execute command: {command}, Error: {e}")

    def show_output(self, output, error):
        """Display the output and error in a new window."""
        output_window = ctk.CTkToplevel(self.root)
        output_window.title("Command Output")
        output_window.geometry("600x400")
        output_window.wm_attributes("-topmost", 1)

        # Center the popup window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 600
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        output_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Make the popup window resizable
        output_window.resizable(True, True)

        text_widget = ctk.CTkTextbox(output_window, wrap="word")
        text_widget.pack(expand=True, fill="both", padx=10, pady=10)

        if output:
            text_widget.insert("end", "OUTPUT:\n" + output + "\n")
        if error:
            text_widget.insert("end", "ERROR:\n" + error + "\n")

        text_widget.configure(state="disabled")

    def get_user_input(self, prompt):
        """Get user input using a custom input dialog."""
        print(f"Creating input dialog with prompt: {prompt}")  # Debugging
        input_dialog = ctk.CTkToplevel(self.root)
        input_dialog.title("Input Required")
        input_dialog.geometry("300x200")
        input_dialog.wm_attributes("-topmost", 1)

        # Center the popup window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 300
        window_height = 200
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        input_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Make the popup window resizable
        input_dialog.resizable(True, True)

        label = ctk.CTkLabel(input_dialog, text=prompt)
        label.pack(pady=10)

        entry = ctk.CTkEntry(input_dialog)
        entry.pack(pady=10)

        user_input = None

        def submit():
            nonlocal user_input
            user_input = entry.get().strip()
            if user_input:
                input_dialog.destroy()
            else:
                messagebox.showerror("Error", "Input cannot be empty.")

        submit_button = ctk.CTkButton(input_dialog, text="Submit", command=submit)
        submit_button.pack(pady=10)

        input_dialog.grab_set()  # Ensure the dialog receives all events
        self.root.wait_window(input_dialog)  # Wait for the dialog to be destroyed

        return user_input

    def open_script_management_dialog(self):
        """Opens a dialog to manage scripts (create/delete/upload)."""
        management_dialog = ctk.CTkToplevel(self.root)
        management_dialog.title("Manage Scripts")
        management_dialog.geometry("400x400")
        management_dialog.wm_attributes("-topmost", 1)

        # Center the popup window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 400
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        management_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Make the popup window resizable
        management_dialog.resizable(True, True)

        create_script_button = ctk.CTkButton(
            management_dialog,
            text="Create Script",
            font=("Super Shiny", 20),
            command=self.create_script_dialog,
        )
        create_script_button.pack(pady=10)

        # Add Upload Script Button
        upload_script_button = ctk.CTkButton(
            management_dialog,
            text="Upload Script",
            font=("Super Shiny", 20),
            command=self.upload_script_dialog,  # Call the new function
        )
        upload_script_button.pack(pady=10)

        # Add Edit Script Button
        edit_script_button = ctk.CTkButton(
            management_dialog,
            text="Edit Script",
            font=("Super Shiny", 20),
            command=self.edit_script_dialog,
        )
        edit_script_button.pack(pady=10)

        delete_button = ctk.CTkButton(
            management_dialog,
            text="Delete Script",
            font=("Super Shiny", 20),
            command=self.delete_script_dialog,
        )
        delete_button.pack(pady=10)

    def upload_script_dialog(self):
        """Handles the script upload process."""
        upload_dialog = ctk.CTkToplevel(self.root)
        upload_dialog.title("Upload Script")
        upload_dialog.geometry("600x400")
        upload_dialog.wm_attributes("-topmost", 1)

        # Center the popup window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 600
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        upload_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Make the popup window resizable
        upload_dialog.resizable(True, True)

        # File Selection
        def select_file():
            filename = filedialog.askopenfilename(
                initialdir="/",
                title="Select a Script File",
                filetypes=(("Shell scripts", "*.sh"), ("All files", "*.*")),
            )
            if filename:
                file_path_label.configure(text=filename)

        select_button = ctk.CTkButton(
            upload_dialog, text="Select Script File", command=select_file
        )
        select_button.pack(pady=5)

        file_path_label = ctk.CTkLabel(upload_dialog, text="No file selected")
        file_path_label.pack(pady=5)

        # Title
        title_label = ctk.CTkLabel(upload_dialog, text="Script Title:")
        title_label.pack(pady=5)
        title_entry = ctk.CTkEntry(upload_dialog)
        title_entry.pack(pady=5)

        # Category
        category_label = ctk.CTkLabel(upload_dialog, text="Category:")
        category_label.pack(pady=5)
        category_entry = ctk.CTkEntry(upload_dialog)
        category_entry.insert(0, "Custom")  # Default category
        category_entry.configure(state="disabled")  # Make it read-only
        category_entry.pack(pady=5)

        def upload_script():
            """Uploads the script to a file and updates the script list."""
            filepath = file_path_label.cget("text")
            title = title_entry.get().strip()
            category = category_entry.get().strip()  # Should always be "Custom"

            if not filepath or not title:
                messagebox.showerror("Error", "File and title are required.")
                return

            try:
                with open(filepath, "r") as script_file:
                    content = script_file.read()

                # Create the custom scripts directory if it doesn't exist
                if not os.path.exists(CUSTOM_SCRIPTS_DIR):
                    os.makedirs(CUSTOM_SCRIPTS_DIR)

                # Create a filename based on the title
                filename = title.replace(" ", "_") + ".sh"  # Replace spaces with underscores
                script_path = os.path.join(CUSTOM_SCRIPTS_DIR, filename)

                # Save the content to the new script file
                with open(script_path, "w") as new_script_file:
                    new_script_file.write(content)

                # Store the script data in the scripts list
                script_data = {
                    "title": title,
                    "category": category,
                    "path": filename,  # Store only the filename
                    "type": "custom",
                    "content": content,  # Store the content in memory
                }

                self.scripts.append(script_data)
                self.save_scripts()
                self.categories = self.group_scripts_by_category()
                self.show_scripts("Custom", self.categories.get("Custom", []))
                upload_dialog.destroy()

            except FileNotFoundError:
                messagebox.showerror("Error", "File not found.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to upload script: {e}")
                logging.error(f"Failed to upload script {title}: {e}")

        upload_button = ctk.CTkButton(
            upload_dialog, text="Upload", command=upload_script
        )
        upload_button.pack(pady=10)

    def edit_script_dialog(self):
        """Opens a dialog to select and edit a script."""
        if not self.scripts:
            messagebox.showinfo("Info", "No scripts to edit.")
            return

        edit_dialog = ctk.CTkToplevel(self.root)
        edit_dialog.title("Edit Script")
        edit_dialog.geometry("800x600")
        edit_dialog.wm_attributes("-topmost", 1)

        # Center the popup window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 800
        window_height = 600
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        edit_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Make the popup window resizable
        edit_dialog.resizable(True, True)

        script_names = [script["title"] for script in self.scripts if script["type"] == "custom"]
        if not script_names:
            messagebox.showinfo("Info", "No custom scripts to edit.")
            edit_dialog.destroy()
            return

        selected_script = tkinter.StringVar(value=script_names[0] if script_names else "")  # Default selection

        script_menu = ctk.CTkOptionMenu(
            edit_dialog,
            values=script_names,
            variable=selected_script
        )
        script_menu.pack(pady=10)

        # Script Content
        content_label = ctk.CTkLabel(edit_dialog, text="Script Content:")
        content_label.pack(pady=5)
        content_text = ctk.CTkTextbox(edit_dialog)
        content_text.pack(pady=5, expand=True, fill="both")

        def load_script_content():
            script_title = selected_script.get()
            script = next((s for s in self.scripts if s["title"] == script_title), None)
            if script:
                content_text.delete("0.0", "end")
                content_text.insert("0.0", script["content"])

        load_button = ctk.CTkButton(edit_dialog, text="Load Script", command=load_script_content)
        load_button.pack(pady=5)

        def save_script():
            script_title = selected_script.get()
            script = next((s for s in self.scripts if s["title"] == script_title), None)
            if script:
                new_content = content_text.get("0.0", "end").strip()
                if not new_content:
                    messagebox.showerror("Error", "Content cannot be empty.")
                    return

                script["content"] = new_content
                script_path = os.path.join(CUSTOM_SCRIPTS_DIR, script["path"])
                try:
                    with open(script_path, "w") as script_file:
                        script_file.write(new_content)
                    self.save_scripts()
                    self.refresh_scripts()
                    edit_dialog.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save script: {e}")
                    logging.error(f"Failed to save script {script_title}: {e}")

        save_button = ctk.CTkButton(edit_dialog, text="Save Script", command=save_script)
        save_button.pack(pady=10)

    def create_script_dialog(self):
        """Handles the script creation process."""
        create_dialog = ctk.CTkToplevel(self.root)
        create_dialog.title("Create Script")
        create_dialog.geometry("800x600")
        create_dialog.wm_attributes("-topmost", 1)

        # Center the popup window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 800
        window_height = 600
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        create_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Make the popup window resizable
        create_dialog.resizable(True, True)

        # Title
        title_label = ctk.CTkLabel(create_dialog, text="Script Title:")
        title_label.pack(pady=5)
        title_entry = ctk.CTkEntry(create_dialog)
        title_entry.pack(pady=5)

        # Category
        category_label = ctk.CTkLabel(create_dialog, text="Category:")
        category_label.pack(pady=5)
        category_entry = ctk.CTkEntry(create_dialog)
        category_entry.insert(0, "Custom")  # Default category
        category_entry.configure(state="disabled")  # Make it read-only
        category_entry.pack(pady=5)

        # Script Content
        content_label = ctk.CTkLabel(create_dialog, text="Script Content:")
        content_label.pack(pady=5)
        content_text = ctk.CTkTextbox(create_dialog)
        content_text.pack(pady=5, expand=True, fill="both")

        def save_script():
            """Saves the script to a file and updates the script list."""
            title = title_entry.get().strip()
            category = category_entry.get().strip()  # Should always be "Custom"
            content = content_text.get("0.0", "end").strip()

            if not title or not content:
                messagebox.showerror("Error", "Title and content are required.")
                return

            # Create the custom scripts directory if it doesn't exist
            if not os.path.exists(CUSTOM_SCRIPTS_DIR):
                os.makedirs(CUSTOM_SCRIPTS_DIR)

            # Create a filename based on the title
            filename = title.replace(" ", "_") + ".sh"  # Replace spaces with underscores
            script_path = os.path.join(CUSTOM_SCRIPTS_DIR, filename)

            try:
                with open(script_path, "w") as script_file:
                    script_file.write(content)

                # Store the script data in the scripts list
                script_data = {
                    "title": title,
                    "category": category,
                    "path": filename,  # Store only the filename
                    "type": "custom",
                    "content": content  # Store the content in memory
                }

                self.scripts.append(script_data)
                self.save_scripts()
                self.categories = self.group_scripts_by_category()
                self.show_scripts("Custom", self.categories.get("Custom", []))
                create_dialog.destroy()

            except Exception as e:
                messagebox.showerror("Error", f"Failed to save script: {e}")
                logging.error(f"Failed to save script {title}: {e}")

        save_button = ctk.CTkButton(create_dialog, text="Save Script",command=save_script)
        save_button.pack(pady=10)

    def delete_script_dialog(self):
        """Opens a dialog to select and delete a script."""
        if not self.scripts:
            messagebox.showinfo("Info", "No scripts to delete.")
            return

        delete_dialog = ctk.CTkToplevel(self.root)
        delete_dialog.title("Delete Script")
        delete_dialog.geometry("300x200")
        delete_dialog.wm_attributes("-topmost", 1)

        # Center the popup window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 300
        window_height = 200
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        delete_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Make the popup window resizable
        delete_dialog.resizable(True, True)

        script_names = [script["title"] for script in self.scripts]
        selected_script = tkinter.StringVar(value=script_names[0])  # Default selection

        script_menu = ctk.CTkOptionMenu(
            delete_dialog,
            values=script_names,
            variable=selected_script
        )
        script_menu.pack(pady=10)

        def delete_selected_script():
            script_title = selected_script.get()
            script_to_delete = next((s for s in self.scripts if s["title"] == script_title), None)

            if script_to_delete:
                confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{script_to_delete['title']}'?")
                if confirm:
                    # Remove the script file if it's a custom script
                    if script_to_delete["type"] == "custom":
                        script_path = os.path.join(CUSTOM_SCRIPTS_DIR, script_to_delete["path"])
                        try:
                            os.remove(script_path)
                        except Exception as e:
                            messagebox.showerror("Error", f"Failed to delete script file: {e}")
                            logging.error(f"Failed to delete script file {script_path}: {e}")

                    self.scripts = [s for s in self.scripts if s != script_to_delete]
                    self.save_scripts()
                    self.categories = self.group_scripts_by_category()
                    self.refresh_scripts()
                    delete_dialog.destroy()
            else:
                messagebox.showerror("Error", "Script not found.")

        delete_button = ctk.CTkButton(
            delete_dialog,
            text="Delete",
            command=delete_selected_script
        )
        delete_button.pack(pady=10)

    def save_scripts(self):
        """Save the scripts to the JSON file."""
        with open(SCRIPTS_CONFIG_FILE, "w") as file:
            json.dump({"scripts": self.scripts}, file)

    def logout(self):
        """Handle logout."""
        if self.ssh:
            self.ssh.close()
            self.ssh = None
        self.main_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)
        messagebox.showinfo("Logout", "You have been logged out.")
        logging.info("User logged out.")


# Main program
if __name__ == "__main__":
    root = ctk.CTk()
    app = SSHApp(root)
    root.mainloop()