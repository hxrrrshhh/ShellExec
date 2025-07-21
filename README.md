# ShellExec

ShellExec is a Python-based SSH client application that allows users to execute shell scripts remotely through a graphical user interface built with CustomTkinter.

## Features

- SSH connection management with credential saving
- Script management with categorized organization
- Custom script creation and editing
- Upload and execute shell scripts remotely
- Light/Dark mode toggle
- Logging functionality

## Getting Started

### Prerequisites

- Python 3.7+
- Required Python packages (see requirements)
- SSH access to target remote systems

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hxrrrshhh/ShellExec.git
   cd ShellExec
   ```

2. Switch to the master branch (default branch):
   ```bash
   git checkout master
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the main application:
```bash
python ShellExec.py
```

## Repository Structure

- `master` - Main development branch (default)
- Python files: Main application code
- `assets/` - UI assets and images
- `themes/` - CustomTkinter theme files
- `fonts/` - Custom fonts
- `scripts.json` - Configuration for predefined scripts
- `credentials.json` - Saved SSH credentials (created at runtime)

## Contributing

When contributing to this repository:

1. Fork the repository
2. Create a feature branch from `master`:
   ```bash
   git checkout master
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
4. Submit a pull request targeting the `master` branch

## Default Branch

This repository uses `master` as the default branch. All new features and fixes should be based on and merged into the `master` branch.

## License

This project is available under standard open source terms.