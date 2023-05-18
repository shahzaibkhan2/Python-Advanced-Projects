# Import os module
import os

# Function to show hidden folders
def show_hidden_folders():
    # Get the current working directory
    path = os.getcwd()

    # List all files and directories, including hidden ones
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.name.startswith('.'):  # Check if it's a hidden folder
                print(entry.name)

# Function to hide folders
def hide_folder(folder_name):
    # Add a dot (.) prefix to hide the folder
    hidden_folder_name = '.' + folder_name

    # Rename the folder
    os.rename(folder_name, hidden_folder_name)
    print(f"{folder_name} is now hidden as {hidden_folder_name}.")

# Function to unhide folders
def unhide_folder(hidden_folder_name):
    # Remove the dot (.) prefix to unhide the folder
    folder_name = hidden_folder_name.lstrip('.')

    # Rename the folder
    os.rename(hidden_folder_name, folder_name)
    print(f"{hidden_folder_name} is now unhidden as {folder_name}.")

# Example for usage
print("Showing hidden folders:")
show_hidden_folders()

# Hide a folder
folder_to_hide = "my_folder"
hide_folder(folder_to_hide)

# Show hidden folders again to verify
print("\nShowing hidden folders:")
show_hidden_folders()

# Unhide a folder
hidden_folder_to_unhide = ".my_folder"
unhide_folder(hidden_folder_to_unhide)

# Show hidden folders again to verify
print("\nShowing hidden folders:")
show_hidden_folders()
