import pyperclip
import re
import keyboard
import time

def increment_number_with_padding(number_str):
    padding = ''
    for char in number_str:
        if char == '0':
            padding += char
        else:
            break
    
    number_part = number_str[len(padding):]
    incremented_number = int(number_part) + 1
    
    incremented_number_str = padding + str(incremented_number)
    
    return incremented_number_str

def handle_clipboard_update(event):
    """Increments the last number in the clipboard content."""
    if event.event_type == 'down' and event.name.lower() == 'v':
        time.sleep(0.1)
        
        clipboard_content = pyperclip.paste()
        clipboard_parts = clipboard_content.split('-')
        last_part = clipboard_parts[-1]
        last_number = re.search(r'\d+$', last_part).group()
        incremented_number = increment_number_with_padding(last_number)

        clipboard_parts[-1] = re.sub(r'\d+$', incremented_number, last_part)

        new_clipboard_content = '-'.join(clipboard_parts)
        pyperclip.copy(new_clipboard_content)

keyboard.on_press(handle_clipboard_update)
print("Listening for 'V' key press; increments the last number after '-' in the clipboard content on each 'V' press.")
print("Press 'F10' to exit the program.")

keyboard.wait('f10')




    
