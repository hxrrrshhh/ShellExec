
# ShellExec 🔐💻

ShellExec is a powerful GUI-based SSH automation tool built with **Python**, **CustomTkinter**, and **Paramiko**. It enables you to securely log into remote Linux machines and execute categorized shell scripts with ease — making server-side automation fast and intuitive.

---

## 🧰 Features

- 🔐 **Secure SSH Login** with saved credentials
- 🗂️ **Categorized Script Management** (Arithmetic, System Monitoring, Networking, etc.)
- 🖱️ **One-click Execution** of scripts remotely
- ✍️ **Custom Script Creation, Upload, Edit, and Deletion**
- 🎨 **Light/Dark Mode Toggle**
- 🖼️ Custom background with themed UI

---

## 📂 Folder Structure

```
ShellExec/
│
├── ShellExec.py / SExec.py           # Main application file
├── scripts.json                      # Script metadata and configuration
├── credentials.json                  # Saved SSH credentials (auto-managed)
├── assets/
│   └── abcde.jpg                     # Background image
├── themes/
│   └── violet.json                   # Theme file
├── scripts/
│   └── *.sh                          # Shell scripts
│
└── logs/
    └── shell_exec.log               # Logging output
```

---

## 🚀 Getting Started

### 1. 📦 Prerequisites

Ensure the following Python libraries are installed:

```bash
pip install customtkinter paramiko pillow
```

### 2. ▶️ Run the App

```bash
python ShellExec.py
```

### 3. 🖥️ Usage

- Enter **hostname**, **username**, and **password** to log in via SSH.
- Browse available script categories and execute them.
- Create or upload your own `.sh` scripts under `Manage Scripts`.

---

## 📜 Script Configuration

Scripts are defined in `scripts.json` with the following structure:

```json
{
  "title": "Addition",
  "description": "Adds two numbers.",
  "category": "Arithmetic",
  "path": "script1.sh",
  "type": "normal",
  "parameters": [
    {
      "name": "num1",
      "prompt": "Enter the first number:"
    },
    {
      "name": "num2",
      "prompt": "Enter the second number:"
    }
  ]
}
```

- `type`: Can be `normal` (executes script by path) or `custom` (executes inlined content).
- `parameters`: Dynamically prompted from the user at runtime.

---

## 🔐 Security Notice

This app stores credentials locally in `credentials.json` after login. **Do not share this file** publicly or commit it to version control. For better security, consider encryption or SSH key authentication in production environments.

---

## 📸 Screenshots

<img width="344" height="288" alt="Screenshot 2025-04-20 225336" src="https://github.com/user-attachments/assets/ea5c8437-024b-4dca-9b8d-b8bd8fecf3a7" />
<img width="833" height="643" alt="Screenshot 2025-04-20 225238" src="https://github.com/user-attachments/assets/037b85b7-f32b-432a-b56e-56db029781b3" />
<img width="1052" height="655" alt="Screenshot 2025-04-20 225221" src="https://github.com/user-attachments/assets/ecc07859-1963-4eb9-b01d-7da5038c6ef8" />
<img width="801" height="635" alt="Screenshot 2025-04-20 225148" src="https://github.com/user-attachments/assets/684caa49-729a-4747-a3c9-593d66aac095" />
<img width="398" height="424" alt="Screenshot 2025-04-20 225107" src="https://github.com/user-attachments/assets/0321aef1-7b76-4825-b588-23fd64229d16" />
<img width="1919" height="1032" alt="Screenshot 2025-04-20 225026" src="https://github.com/user-attachments/assets/8ad3fe1f-8a54-4d90-89c0-bad9b37aefc3" />
<img width="1919" height="1031" alt="Screenshot 2025-04-20 225004" src="https://github.com/user-attachments/assets/a808e324-8a88-4129-b432-5206a3accf63" />
<img width="1919" height="1027" alt="Screenshot 2025-04-20 224938" src="https://github.com/user-attachments/assets/fa7f7a3e-6d2c-4943-8f99-a595e607a1cd" />
<img width="1919" height="1033" alt="Screenshot 2025-04-20 224838" src="https://github.com/user-attachments/assets/71b4b5f5-7d64-4e20-897a-eb6100109db1" />
<img width="1917" height="1030" alt="Screenshot 2025-04-20 224803" src="https://github.com/user-attachments/assets/bcc91ecb-5d3d-4fc0-95f5-44a4faa827ae" />



---

## 👨‍💻 Developer

**Harsh Sharma** 

---

## 📄 License

This project is licensed under the MIT License — feel free to use and modify for your own purposes.

---

## 🙌 Contributions

Feel free to fork this repo, submit pull requests, or suggest features via GitHub Issues.
