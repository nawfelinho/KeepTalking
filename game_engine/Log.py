import threading
from Event import Event, Level
import  tkinter as tk

class Log:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Log, cls).__new__(cls)
                cls._instance._initialized = False
            return cls._instance

    def __init__(self, text_box):
        with self._lock:
            if not self._initialized:
                self.text_box = text_box
                self._initialized = True

    def add(self, e: Event):
        match e.get_level():
            case Level.INFO:
                self.text_box.config(foreground='black')
                self.text_box.insert(tk.END, e.to_string())
            case Level.WARNING:
                self.text_box.config(foreground='orange')
                self.text_box.insert(tk.END, e.to_string())
            case Level.ERROR:
                self.text_box.config(foreground='red')
                self.text_box.insert(tk.END, e.to_string())
            case Level.GAMEPLAY:
                self.text_box.config(foreground='blue')
                self.text_box.insert(tk.END, e.to_string())