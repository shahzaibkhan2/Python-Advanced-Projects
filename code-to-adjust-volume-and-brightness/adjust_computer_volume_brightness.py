# Import subprocess module
import subprocess

# Function to set volume
def set_volume(volume):
    """
    Adjusts the computer volume using the 'osascript' command on macOS or 'nircmd' on Windows.
    """
    try:
        # macOS command
        subprocess.run(["osascript", "-e", f"set volume output volume {volume}"], check=True)
    except FileNotFoundError:
        try:
            # Windows command (requires 'nircmd' utility in the same directory as the script)
            subprocess.run(["nircmd.exe", "setsysvolume", str(volume)], check=True)
        except FileNotFoundError:
            print("Error: Volume adjustment is not supported on this operating system.")

# Function to set brightness
def set_brightness(brightness):
    """
    Adjusts the computer brightness using the 'osascript' command on macOS or 'nircmd' on Windows.
    """
    try:
        # macOS command
        subprocess.run(["osascript", "-e", f"tell application \"System Events\" to set brightness of first display to {brightness}"], check=True)
    except FileNotFoundError:
        try:
            # Windows command (requires 'nircmd' utility in the same directory as the script)
            subprocess.run(["nircmd.exe", "setbrightness", str(brightness)], check=True)
        except FileNotFoundError:
            print("Error: Brightness adjustment is not supported on this operating system.")

# Adjust volume to 70% (0-100 range)
set_volume(70)

# Adjust brightness to 90% (0-100 range)
set_brightness(90)
