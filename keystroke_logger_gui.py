import json
from datetime import datetime
from pynput import keyboard
import tkinter as tk

text_log = "keylog.txt"
json_log = "keylog.json"

listener = None
active = False

def log_text(data):
    with open(text_log, "a") as f:
        f.write(data + "\n")

def log_json(data):
    with open(json_log, "a") as f:
        f.write(json.dumps(data) + "\n")

def start():
    global listener, active
    if active:
        return

    active = True
    log_text(f"Session started: {datetime.now()}")
    log_json({"session_start": str(datetime.now())})

    def on_press(key):
        record = {
            "time": str(datetime.now()),
            "key": str(key)
        }
        log_text(f"{record['time']} - {record['key']}")
        log_json(record)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    status.config(text="Logging: ON")

def stop():
    global active, listener
    if not active:
        return

    active = False
    if listener:
        listener.stop()

    log_text(f"Session ended: {datetime.now()}")
    log_json({"session_end": str(datetime.now())})
    status.config(text="Logging: OFF")

def close():
    stop()
    root.destroy()

root = tk.Tk()
root.title("Keystroke Logger Demo")
root.geometry("350x220")

tk.Label(root, text="Keystroke Logging Demo", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Start", width=20, command=start).pack(pady=5)
tk.Button(root, text="Stop", width=20, command=stop).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=close).pack(pady=5)

status = tk.Label(root, text="Logging: OFF")
status.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
