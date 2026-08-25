import sys
import shutil
import subprocess
import platform


# --------------------------------------------------
# Mehrooons Toolkit
# Usage:
#   python main.py --nettest
#   python main.py --install vscode
#   python main.py --install spotify
# --------------------------------------------------

APPS = {
    "spotify": {
        "choco": "spotify",
        "winget": "Spotify.Spotify",
    },
    "vscode": {
        "choco": "vscode",
        "winget": "Microsoft.VisualStudioCode",
    },
    "discord": {
        "choco": "discord",
        "winget": "Discord.Discord",
    },
    "7zip": {
        "choco": "7zip",
        "winget": "7zip.7zip",
    },
    "firefox": {
        "choco": "firefox",
        "winget": "Mozilla.Firefox",
    },
    "git": {
        "choco": "git",
        "winget": "Git.Git",
    },
    "python": {
        "choco": "python",
        "winget": "Python.Python.3",
    },
    "node": {
        "choco": "nodejs",
        "winget": "OpenJS.NodeJS",
    },
}


def command_exists(command):
    """Check whether a command exists in PATH."""
    return shutil.which(command) is not None


def run(command):
    """Run a command and return its exit code."""
    try:
        result = subprocess.run(command)
        return result.returncode
    except FileNotFoundError:
        return 1
    except KeyboardInterrupt:
        print("\n[!] Cancelled.")
        return 130
    except Exception as error:
        print(f"[!] Error: {error}")
        return 1


def nettest():
    """Basic internet connectivity test."""
    import socket

    print("\n=== Internet Test ===")

    tests = [
        ("Cloudflare", "1.1.1.1"),
        ("Google DNS", "8.8.8.8"),
    ]

    for name, host in tests:
        try:
            socket.create_connection((host, 443), timeout=5)
            print(f"[+] {name}: ONLINE")
        except OSError:
            print(f"[-] {name}: OFFLINE")

    try:
        socket.gethostbyname("google.com")
        print("[+] DNS: WORKING")
    except socket.gaierror:
        print("[-] DNS: FAILED")


def install_app(app):
    """Install an application using Chocolatey, then winget."""

    app = app.lower().strip()

    if app not in APPS:
        print(f"\n[!] Unknown application: {app}")
        print("\nSupported applications:")

        for name in APPS:
            print(f"  - {name}")

        return 1

    package = APPS[app]

    print(f"\n=== Installing {app} ===")

    # ----------------------------------------------
    # Chocolatey FIRST
    # ----------------------------------------------

    if command_exists("choco"):
        print("[+] Chocolatey detected.")
        print(f"[*] Trying Chocolatey: {package['choco']}")

        result = run([
            "choco",
            "install",
            package["choco"],
            "-y",
            "--no-progress",
        ])

        if result == 0:
            print(f"\n[+] {app} installed successfully with Chocolatey.")
            return 0

        print("[-] Chocolatey failed.")
    else:
        print("[-] Chocolatey not found.")

    # ----------------------------------------------
    # winget FALLBACK
    # ----------------------------------------------

    if command_exists("winget"):
        print("[+] winget detected.")
        print(f"[*] Trying winget: {package['winget']}")

        result = run([
            "winget",
            "install",
            "--id",
            package["winget"],
            "--exact",
            "--accept-source-agreements",
            "--accept-package-agreements",
        ])

        if result == 0:
            print(f"\n[+] {app} installed successfully with winget.")
            return 0

        print("[-] winget failed.")
    else:
        print("[-] winget not found.")

    print("\n[!] Installation failed.")
    print("[!] Neither package manager could install the application.")

    return 1


def sysinfo():

    if shutil.which("node"):
    node_version = subprocess.check_output(
        ["node", "--version"],
        text=True
    ).strip()
    else:
        node_version = "Not installed"
    
    print("\n=== System Information ===")
    print(f"OS:           {platform.system()}")
    print(f"Version:      {platform.version()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Python:       {platform.python_version()}")
    print(f"Node.js:      {node_version}")


def help_menu():
    print("""
=== Mehrooons Toolkit ===

Commands:

  --nettest
      Test internet connectivity.

  --sysinfo
      Show system information.

  --install <app>
      Install an application.

Supported applications:

  spotify
  vscode
  discord
  7zip
  firefox
  git
  python
  node
""")


def main():
    # ----------------------------------------------
    # Windows check
    # ----------------------------------------------

    if platform.system() != "Windows":
        print("[!] This toolkit currently supports Windows only.")
        return 1

    args = sys.argv[1:]

    if not args:
        help_menu()
        return 0

    command = args[0].lower()

    # ----------------------------------------------
    # Commands
    # ----------------------------------------------

    if command == "--nettest":
        nettest()
        return 0

    if command == "--sysinfo":
        sysinfo()
        return 0

    if command == "--download":
        if len(args) < 2:
            print("[!] Missing application name.")
            print("Usage: --install <app>")
            return 1

        return install_app(args[1])

    if command in ("--help", "-h", "/?"):
        help_menu()
        return 0

    print(f"[!] Unknown command: {command}")
    help_menu()

    return 1


if __name__ == "__main__":
    sys.exit(main())
