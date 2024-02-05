import tkinter as tk
from tkinter import ttk
import pyperclip
import keyboard
import time

copy_list = [
    {"copy_id": "XxX", "copy_value": "111"},
    {"copy_id": "YyY", "copy_value": "222"},
    {"copy_id": "ZzZ", "copy_value": "333"},
    {"copy_id": "WwW", "copy_value": "444"}
]
index = 0

def show_next_and_copy():
    global index
    if index < len(copy_list):
        selected_item = copy_list[index]
        pyperclip.copy(selected_item["copy_value"])
        label.config(text=selected_item["copy_id"])
        print(f"{selected_item['copy_id']} is displayed, {selected_item['copy_value']} is copied to clipboard.")
        index += 1
    else:
        label.config(text="All items have been displayed")
        print("Entire list has been copied. Terminating script.")
        keyboard.unhook_all()
        time.sleep(1.5)
        root.destroy()

def wait_then_show_and_copy():
    time.sleep(0.2)
    show_next_and_copy()

root = tk.Tk()
root.title("CopyPaster")

window_width = 1000
window_height = 120
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width / 2) - (window_width / 2)
y_position = (0)
root.geometry(f"{window_width}x{window_height}+{int(x_position)}+{int(y_position)}")

root.attributes("-topmost", True)

label = ttk.Label(root, text="", font=('Arial', 48, 'bold'), foreground='red')
label.pack(pady=20)

keyboard.add_hotkey('ctrl+v', wait_then_show_and_copy)

wait_then_show_and_copy()

print("Copy list operation started. Please continue with 'Ctrl+V'.")
root.mainloop()