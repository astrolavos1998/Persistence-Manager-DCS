import os
import tkinter as tk
from tkinter import ttk, messagebox

# Lines to enable persistence
enable_lines = [
    "--	sanitizeModule('os')",
    "--	sanitizeModule('io')",
    "--	sanitizeModule('lfs')",
    "--	_G['require'] = nil",
    "--	_G['loadlib'] = nil",
    "--	_G['package'] = nil"
]

# Lines to disable persistence
disable_lines = [
    "	sanitizeModule('os')",
    "	sanitizeModule('io')",
    "	sanitizeModule('lfs')",
    "	_G['require'] = nil",
    "	_G['loadlib'] = nil",
    "	_G['package'] = nil"
]

# Function to find the MissionScripting.lua file
def find_mission_scripting_file():
    # Common installation directories for DCS World
    common_paths = [
        r"C:\Program Files\Eagle Dynamics\DCS World",
        r"C:\Program Files (x86)\Eagle Dynamics\DCS World",
        r"C:\Users",  # In case of custom installations in user directories
    ]

    # Search each directory recursively
    for base_path in common_paths:
        if os.path.exists(base_path):
            for root, dirs, files in os.walk(base_path):
                if "MissionScripting.lua" in files:
                    return os.path.join(root, "MissionScripting.lua")

    # Fallback: Search the entire C:\ drive
    try:
        for root, dirs, files in os.walk("C:\\"):
            if "MissionScripting.lua" in files:
                return os.path.join(root, "MissionScripting.lua")
    except Exception as e:
        messagebox.showwarning("Warning", f"Search encountered an issue: {e}")

    # If not found, return None
    return None

# Function to enable persistence
def enable_persistence():
    mission_scripting_file = find_mission_scripting_file()
    if not mission_scripting_file:
        messagebox.showerror("Error", "MissionScripting.lua file not found.")
        return

    try:
        with open(mission_scripting_file, "r") as file:
            lines = file.readlines()

        # Replace lines
        for i in range(len(lines)):
            if "sanitizeModule('os')" in lines[i]:
                lines[i] = enable_lines[0] + "\n"
            elif "sanitizeModule('io')" in lines[i]:
                lines[i] = enable_lines[1] + "\n"
            elif "sanitizeModule('lfs')" in lines[i]:
                lines[i] = enable_lines[2] + "\n"
            elif "_G['require'] = nil" in lines[i]:
                lines[i] = enable_lines[3] + "\n"
            elif "_G['loadlib'] = nil" in lines[i]:
                lines[i] = enable_lines[4] + "\n"
            elif "_G['package'] = nil" in lines[i]:
                lines[i] = enable_lines[5] + "\n"

        with open(mission_scripting_file, "w") as file:
            file.writelines(lines)

        # Show success message in green
        show_colored_message("Success", "Persistence Enabled. Now you can save your mission in DCS World!", "green")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to enable persistence: {e}")

# Function to disable persistence
def disable_persistence():
    mission_scripting_file = find_mission_scripting_file()
    if not mission_scripting_file:
        messagebox.showerror("Error", "MissionScripting.lua file not found.")
        return

    try:
        with open(mission_scripting_file, "r") as file:
            lines = file.readlines()

        # Replace lines
        for i in range(len(lines)):
            if "--	sanitizeModule('os')" in lines[i]:
                lines[i] = disable_lines[0] + "\n"
            elif "--	sanitizeModule('io')" in lines[i]:
                lines[i] = disable_lines[1] + "\n"
            elif "--	sanitizeModule('lfs')" in lines[i]:
                lines[i] = disable_lines[2] + "\n"
            elif "--	_G['require'] = nil" in lines[i]:
                lines[i] = disable_lines[3] + "\n"
            elif "--	_G['loadlib'] = nil" in lines[i]:
                lines[i] = disable_lines[4] + "\n"
            elif "--	_G['package'] = nil" in lines[i]:
                lines[i] = disable_lines[5] + "\n"

        with open(mission_scripting_file, "w") as file:
            file.writelines(lines)

        # Show success message in red
        show_colored_message("Success", "Persistence Disabled. Now you cannot save your mission in DCS World!", "red")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to disable persistence: {e}")

# Function to show a colored message with an [OK] button
def show_colored_message(title, message, color):
    # Create a new window for the message
    message_window = tk.Toplevel(root)
    message_window.title(title)
    message_window.geometry("500x150")
    message_window.configure(bg="#2d2d2d")

    # Center the popup window on the screen
    window_width = 500
    window_height = 150
    screen_width = message_window.winfo_screenwidth()
    screen_height = message_window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    message_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Display the message in the specified color
    label = tk.Label(message_window, text=message, font=("Arial", 12), bg="#2d2d2d", fg=color)
    label.pack(pady=20)

    # Add an [OK] button to close the window
    ok_button = ttk.Button(message_window, text="OK", command=message_window.destroy)
    ok_button.pack(pady=10)

# Function to exit the program
def exit_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("DCS World Persistence Manager® 2025© for LOCK-ON GREECE by =GR= Astr0")

# Set window size and center it
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Dark mode theme
root.configure(bg="#2d2d2d")
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#2d2d2d", foreground="white")
style.configure("TButton", background="#4d4d4d", foreground="white", relief="flat")
style.map("TButton", background=[("active", "#5d5d5d")])

# Custom title label
title_label = tk.Label(root, text="DCS World Persistence Manager", font=("Arial", 16, "bold"), bg="#2d2d2d", fg="blue")
title_label.pack(pady=20)

# Instructions label
instructions_label = tk.Label(root, text="Click 'Enable' to allow saving missions or 'Disable' to restrict saving.", font=("Arial", 12), bg="#2d2d2d", fg="white")
instructions_label.pack(pady=10)

# Enable button
enable_button = ttk.Button(root, text="Enable", command=enable_persistence)
enable_button.pack(pady=10)

# Disable button
disable_button = ttk.Button(root, text="Disable", command=disable_persistence)
disable_button.pack(pady=10)

# Exit button
exit_button = ttk.Button(root, text="Exit", command=exit_program)
exit_button.pack(pady=10)

# Run the application
root.mainloop()
