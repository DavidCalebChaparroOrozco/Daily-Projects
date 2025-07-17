# Import necessary libraries
import os
import platform
import subprocess
import sys

# Clear the terminal screen
def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

# Check if a command is available and return its version
def check_installed(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, shell=True)
        return True, result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False, ""

# Prompt the user to confirm installation
def prompt_install(software_name):
    while True:
        choice = input(f"\n{software_name} is not installed. Do you want to install it? (y/n): ").lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        print("Please enter 'y' or 'n'.")

# Check if Docker and Docker Compose are installed
def check_docker_and_compose():
    docker_installed, docker_version = check_installed("docker --version")
    compose_installed, compose_version = check_installed("docker compose version")

    if not compose_installed:
        compose_installed, compose_version = check_installed("docker-compose --version")

    return docker_installed, docker_version, compose_installed, compose_version

# Install Docker and Docker Compose on Linux
def install_linux():
    docker_installed, _, compose_installed, _ = check_docker_and_compose()

    if docker_installed and compose_installed:
        print("\nDocker and Docker Compose are already installed.")
        return

    if not prompt_install("Docker and Docker Compose"):
        return

    print("\nInstalling Docker and Docker Compose on Linux...")
    commands = [
        "sudo apt-get update",
        "sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common",
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
        'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"',
        "sudo apt-get update",
        "sudo apt-get install -y docker-ce docker-ce-cli containerd.io",
        'sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose',
        "sudo chmod +x /usr/local/bin/docker-compose",
        f"sudo usermod -aG docker {os.getenv('USER')}"
    ]

    for cmd in commands:
        subprocess.run(cmd, shell=True)

    print("\nDocker and Docker Compose installation completed on Linux.")

# Install Docker Desktop on macOS
def install_mac():
    docker_installed, _, compose_installed, _ = check_docker_and_compose()

    if docker_installed and compose_installed:
        print("\nDocker and Docker Compose are already installed.")
        return

    if not prompt_install("Docker Desktop (includes Docker and Docker Compose)"):
        return

    print("\nInstalling Docker Desktop on macOS...")
    if not check_installed("brew")[0]:
        print("Homebrew not found. Installing Homebrew first...")
        subprocess.run('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"', shell=True)

    subprocess.run(["brew", "install", "--cask", "docker"])
    print("Docker Desktop installed. Please launch it from the Applications folder.")

# Install Docker Desktop on Windows
def install_windows():
    docker_installed, _, compose_installed, _ = check_docker_and_compose()

    docker_path = os.path.expandvars(r'%ProgramFiles%\Docker\Docker\Docker Desktop.exe')
    if os.path.exists(docker_path):
        print("\nDocker Desktop is already installed on the system, but may not be initialized.")
        print("Please open Docker Desktop manually at least once to complete setup.")
        return

    if docker_installed and compose_installed:
        print("\nDocker and Docker Compose are already installed.")
        return

    if not prompt_install("Docker Desktop (includes Docker and Docker Compose)"):
        return

    print("\nInstalling Docker Desktop on Windows...")

    try:
        subprocess.run(['net', 'session'], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("\nError: Please run this script as Administrator.")
        return

    installer_path = os.path.join(os.environ['TEMP'], 'DockerDesktopInstaller.exe')
    if not os.path.exists(installer_path):
        print("Downloading Docker Desktop installer...")
        subprocess.run([
            'curl', '-L', 'https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe',
            '-o', installer_path
        ])

    print(f"\nInstaller downloaded to: {installer_path}")
    os.startfile(installer_path)
    print("Docker Desktop installer launched. Follow the on-screen instructions.")

# Check and display Docker and Docker Compose installation status
def post_installation_check():
    docker_installed, docker_version, compose_installed, compose_version = check_docker_and_compose()

    print("\nInstallation result:")
    print(f"Docker: {docker_version if docker_installed else 'Not installed or not initialized.'}")
    print(f"Docker Compose: {compose_version if compose_installed else 'Not installed or not initialized.'}")

    if platform.system() == "Windows":
        docker_path = os.path.expandvars(r'%ProgramFiles%\Docker\Docker\Docker Desktop.exe')
        if os.path.exists(docker_path):
            print("\nNote: Docker Desktop is installed but may not have been initialized yet.")
            print("Please open Docker Desktop manually and restart your terminal to access docker commands.")

# Main menu for selecting the OS and installing Docker
def main():
    while True:
        clear_screen()
        print("="*50)
        print(" Docker & Docker Compose Installer by David Caleb ")
        print("="*50)
        print("\nSelect your operating system:")
        print("1. Linux")
        print("2. macOS")
        print("3. Windows")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '1':
            install_linux()
        elif choice == '2':
            install_mac()
        elif choice == '3':
            install_windows()
        elif choice == '4':
            print("Exiting the installer.")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")
            continue

        post_installation_check()
        input("\nPress Enter to return to the menu...")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nInstallation cancelled by user.")
        sys.exit(1)