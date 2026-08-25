# Mehrooons Toolkit

A lightweight Windows CLI toolkit that runs directly from a Python script hosted on GitHub.

No GUI. No installer required.

## 🚀 Quick Start

Run the toolkit directly from PowerShell:

```powershell
irm https://raw.githubusercontent.com/<USER>/<REPO>/main/main.py | python -
```

You can also pass a command directly:

```powershell
irm https://raw.githubusercontent.com/<USER>/<REPO>/main/main.py | python - --nettest
```

## 📦 Commands

### Internet Test

```powershell
irm https://raw.githubusercontent.com/<USER>/<REPO>/main/main.py | python - --nettest
```

Tests basic internet connectivity and DNS.

### System Information

```powershell
irm https://raw.githubusercontent.com/<USER>/<REPO>/main/main.py | python - --sysinfo
```

Displays:

* Operating system
* Windows version
* CPU architecture
* Python version

### Install Applications

```powershell
irm https://raw.githubusercontent.com/<USER>/<REPO>/main/main.py | python - --install <app>
```

The installer uses:

1. **Chocolatey** first
2. **winget** as a fallback

Example:

```powershell
irm https://raw.githubusercontent.com/<USER>/<REPO>/main/main.py | python - --install vscode
```

Other supported applications:

```text
spotify
vscode
discord
7zip
firefox
git
python
node
```

## 🛠️ How Installation Works

When you run:

```text
--install vscode
```

the toolkit checks for Chocolatey.

```text
Chocolatey found?
       │
   ┌───┴───┐
  YES      NO
   │        │
   ▼        ▼
 Choco    Check winget
   │        │
   └───┬────┘
       ▼
    Install
```

If Chocolatey is unavailable or fails, the toolkit automatically tries winget.

Package IDs are mapped separately because Chocolatey and winget use different package identifiers.

## 💻 Requirements

* Windows
* Python 3.x
* PowerShell
* Chocolatey and/or winget for application installation

Python itself can be downloaded from the official Python website if it isn't already installed.

## 📁 Project Structure

```text
mehrooons-toolkit/
│
├── main.py
└── README.md
```

## ⚠️ Security

This project executes Python code downloaded from a GitHub repository.

Only run the command if you trust the repository and have reviewed its source code.

The installer uses an explicit application allowlist rather than directly executing arbitrary package names as shell commands.

## 🧪 Development

Clone the repository:

```powershell
git clone https://github.com/<USER>/<REPO>.git
cd <REPO>
```

Run locally:

```powershell
python main.py --help
```

Test the internet checker:

```powershell
python main.py --nettest
```

Test system information:

```powershell
python main.py --sysinfo
```

## 📜 License

Choose a license for the project before distributing it publicly.

---

Made by **Mehrooons** 🗿
