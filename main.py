# Import modules
import platform
import time
import pyautogui
import pyperclip
import keyboard
from playsound import playsound

# Lists of shortcut inputs and outputs
input_list = [
    "ac",
    "ad",
    "c",
    "d",
    "h",
    "s",
    "@"]
output_list = [
    "accessibility",
    "Advisory Committee for Persons with Disabilities",
    "committee",
    "disabilities",
    "City of Hamilton",
    "successfully",
    "Best regards,\nJames LastName\nMcMaster University\n(905)525-9140"]

# NOTE can be converted into a file
def print_shortcuts(input, output):
    for i in input:
        idx = input_list.index(i)
        print("Key:", input[idx], ", Output:", output[idx])

# Determines what key is used to paste
def paste_key():
    # Command for Mac
    if platform.system() == "Darwin":
        key = "command"
    # Ctrl for Windows
    else:
        key = "ctrl"
    return key

# Gets output based on input
def output_select(shortcut):
    try:
        # Gets output from index of input
        idx = input_list.index(shortcut)
        output = output_list[idx]
    except:
        # If it doesn't exist, return NA
        output = "NA"
    return output

# Copy to clipboard
def copy_to_clip(txt):
    return pyperclip.copy(txt)

# Main function
def main():
    while True:
        # Activate program
        if keyboard.read_key() == "=":
            # Set errors to 0
            errors = 0
            # Play activation sound
            playsound('/Users/mihanbandara/Downloads/notification.wav')
            # Tell user that the program is active
            print("Activated")
            # Always running
            while True:
                # User inputs shortcut key(s)
                shortcut = input()
                # Output is based on output function
                output = output_select(shortcut)
                if keyboard.read_key() == "enter":
                    time.sleep(1)
                    # If shortcut does not exist, print that
                    if output == "NA":
                        print("Shortcut does not exist")
                        # When the shortcut is incorrect increase the errors counter by 1
                        errors = errors+1
                        # When the errors counter is 3 then remind the user what the shortcuts are
                        if errors == 3:
                            print(print_shortcuts(input_list, output_list))
                            # Set errors to 0
                            errors = 0
                    # If shortcut does exist
                    else:
                        copy_to_clip(output)
                        # Print that the output has been copied
                        print(output, "copied to clipboard")
                        # Paste delay
                        time.sleep(3)
                        # Paste from clipboard to cursor
                        with pyautogui.hold(paste_key()):
                            pyautogui.press(['v'])
                        errors = 0

main()
