# 🛠️ Mehrooons Toolkit

A lightweight Windows CLI toolkit written in Python.

No GUI. No installer. Just run a command from PowerShell and go.

## 🚀 Quick Start

Run Mehrooons Toolkit directly from PowerShell:

```powershell
irm https://raw.githubusercontent.com/Mehrooons/Toolkit/refs/heads/main/sourceCode.py | python -
```

You can also run a specific command immediately.

## 📡 Internet Test

Test your internet connection and DNS:

```powershell
irm https://raw.githubusercontent.com/Mehrooons/Toolkit/refs/heads/main/sourceCode.py | python - --nettest
```

## 💻 System Information

Display basic system information:

```powershell
irm https://raw.githubusercontent.com/Mehrooons/Toolkit/refs/heads/main/sourceCode.py | python - --sysinfo
```

## 📦 Install Applications

Mehrooons Toolkit can install supported applications using:

1. **Chocolatey**
2. **winget** as a fallback

Syntax:

```powershell
irm https://raw.githubusercontent.com/Mehrooons/Toolkit/refs/heads/main/sourceCode.py | python - --download <app>
```

### Examples

Install Spotify:

```powershell
irm https://raw.githubusercontent.com/Mehrooons/Toolkit/refs/heads/main/sourceCode.py | python - --download spotify
```

Install VS Code:

```powershell
irm https://raw.githubusercontent.com/Mehrooons/Toolkit/refs/heads/main/sourceCode.py | python - --download vscode
```

### Supported Apps

| App                | Command              |
| ------------------ | -------------------- |
| Spotify            | `--download spotify` |
| Visual Studio Code | `--download vscode`  |
| Discord            | `--download discord` |
| 7-Zip              | `--download 7zip`    |
| Firefox            | `--download firefox` |
| Git                | `--download git`     |
| Python             | `--download python`  |
| Node.js            | `--download node`    |

## 🔄 Installation Logic

When an app is requested:

```text
--download <app>
       │
       ▼
Check Chocolatey
       │
   ┌───┴───┐
   │       │
 Found   Not Found
   │       │
   ▼       ▼
Install   Check winget
   │       │
   │   ┌───┴───┐
   │   │       │
   │  Found   Not Found
   │   │       │
   │   ▼       ▼
   │ Install  Error
   │
   ▼
 Done
```

Chocolatey is always attempted first. If it isn't installed or the installation fails, the toolkit falls back to winget.

## 🖥️ Requirements

* Windows
* Python 3.x
* PowerShell
* Chocolatey and/or winget for application installation

## 🧪 Run Locally

Clone the repository:

```powershell
git clone https://github.com/Mehrooons/Toolkit.git
cd Toolkit
```

Run the toolkit:

```powershell
python sourceCode.py --help
```

Test the internet checker:

```powershell
python sourceCode.py --nettest
```

Test system information:

```powershell
python sourceCode.py --sysinfo
```

Install an application:

```powershell
python sourceCode.py --download vscode
```

## ⚠️ Security

The quick-start command downloads Python source code directly from this repository and executes it locally.

**Only run it if you trust the repository and have reviewed the source code.**

The application installer uses an explicit list of supported applications instead of passing arbitrary package names directly to the shell.

## 📁 Project Structure

```text
Toolkit/
├── sourceCode.py
└── README.md
```

## 📜 License

Add your preferred license before distributing the project.

---

Made by **Mehrooons** 🗿
