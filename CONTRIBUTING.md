# Contributing to ShellExec

Thank you for your interest in contributing to ShellExec! This document provides guidelines for contributing to the project.

## Development Workflow

### Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/ShellExec.git
   cd ShellExec
   ```
3. Set up the upstream remote:
   ```bash
   git remote add upstream https://github.com/hxrrrshhh/ShellExec.git
   ```
4. Switch to the master branch (default branch):
   ```bash
   git checkout master
   ```

### Making Changes

1. Create a new branch for your feature or bugfix from master:
   ```bash
   git checkout master
   git pull upstream master
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

3. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Create a Pull Request targeting the `master` branch

### Branch Structure

- `master` - The main development branch (default)
- Feature branches should be created from and merged back into `master`
- All pull requests should target the `master` branch

### Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Ensure your code is compatible with Python 3.8+

### Testing

- Test your changes thoroughly before submitting
- Ensure the application runs without errors
- Verify SSH functionality works as expected

### Pull Request Guidelines

1. Ensure your PR targets the `master` branch
2. Provide a clear description of the changes
3. Reference any related issues
4. Update documentation if necessary

## Questions?

If you have questions about contributing, please open an issue for discussion.