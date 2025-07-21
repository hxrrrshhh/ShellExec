
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
<img width="1919" height="1033" alt="Screenshot 2025-04-20 224838" src="https://github.com/user-attachments/assets/1b244490-0042-4a01-b422-9942b45f826d" />
<img width="1917" height="1030" alt="Screenshot 2025-04-20 224803" src="https://github.com/user-attachments/assets/ffc9964e-fb74-458c-a1a5-17e95e65de76" />
<img width="344" height="288" alt="Screenshot 2025-04-20 225336" src="https://github.com/user-attachments/assets/ba8805bd-2d22-4882-9e94-b7e19e04a3f1" />
<img width="833" height="643" alt="Screenshot 2025-04-20 225238" src="https://github.com/user-attachments/assets/9f75a497-a0b0-4741-a7e2-76f67960e4fe" />
<img width="1052" height="655" alt="Screenshot 2025-04-20 225221" src="https://github.com/user-attachments/assets/a198aa32-60a2-45dd-a1d9-b131e03d0a46" />
<img width="801" height="635" alt="Screenshot 2025-04-20 225148" src="https://github.com/user-attachments/assets/d10e079a-df8d-46d1-85ce-15d06595a973" />
<img width="398" height="424" alt="Screenshot 2025-04-20 225107" src="https://github.com/user-attachments/assets/b53fef54-3d71-4409-b82a-c51106d68e7c" />
<img width="1919" height="1032" alt="Screenshot 2025-04-20 225026" src="https://github.com/user-attachments/assets/ba56e8f6-e592-490d-bdd7-4610ee5223cd" />
<img width="1919" height="1031" alt="Screenshot 2025-04-20 225004" src="https://github.com/user-attachments/assets/7550e1a2-e0e9-4244-ab62-195271f190a2" />
<img width="1919" height="1027" alt="Screenshot 2025-04-20 224938" src="https://github.com/user-attachments/assets/e2cf7e05-7f96-4c1f-9c0d-0052a5d622da" />



---

## 👨‍💻 Developer

**Harsh Sharma** 

---

## 📄 License

This project is licensed under the MIT License — feel free to use and modify for your own purposes.

---

## 🙌 Contributions

Feel free to fork this repo, submit pull requests, or suggest features via GitHub Issues.
