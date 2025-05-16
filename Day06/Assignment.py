import os
import pywhatkit
import subprocess
import platform
from datetime import datetime

def show_desktop_files():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    items = os.listdir(desktop_path)
    visible_items = [item for item in items if not item.startswith('.')]
    print("Files/Folders on Desktop:")
    for item in visible_items:
        print(item)

def create_file():
    filename = input("Enter file name (with extension): ")
    path = os.path.join(os.path.expanduser("~"), "Desktop", filename)
    with open(path, "w") as f:
        f.write("File created by user command.")
    print(f"File created at: {path}")

def create_folder():
    folder_name = input("Enter folder name: ")
    path = os.path.join(os.path.expanduser("~"), "Desktop", folder_name)
    os.makedirs(path, exist_ok=True)
    print(f"Folder created at: {path}")

def send_whatsapp_message():
    message = input("Enter message to send on WhatsApp: ")
    now = datetime.now()
    hour = now.hour
    minute = now.minute + 2  # Send 2 mins later (required by pywhatkit)
    pywhatkit.sendwhatmsg("+918068422452", message, hour, minute)
    print("WhatsApp message scheduled.")

def shutdown_system():
    confirm = input("Are you sure you want to shut down the system? (yes/no): ")
    if confirm.lower() == "yes":
        system_os = platform.system()
        if system_os == "Windows":
            os.system("shutdown /s /t 1")
        elif system_os == "Linux":
            os.system("shutdown -h now")
        elif system_os == "Darwin":
            os.system("osascript -e 'tell application \"System Events\" to shut down'")
        else:
            print("Unsupported OS.")
    else:
        print("Shutdown canceled.")


def main():
    print("""
    1 - Show files/folders on Desktop
    2 - Create a file on Desktop
    3 - Create a folder on Desktop
    4 - Send WhatsApp message
    5 - Shut down system
    """)
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        show_desktop_files()
    elif choice == '2':
        create_file()
    elif choice == '3':
        create_folder()
    elif choice == '4':
        send_whatsapp_message()
    elif choice == '5':
        shutdown_system()
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
