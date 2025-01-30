import threading
import tkinter as tk
from tkinter import ttk

from CanInterface import CanInterface
from Checker import Checker
from ColorNode import ColorNode
from DistanceNode import DistanceNode
from VoiceNode import VoiceNode
from Log import Log

class Engine:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2500x1400")

        self.start_button = ttk.Button(root, text="Start", command=self.start)
        self.quit_button = ttk.Button(root, text="Quit", command=self.shutdown)
        self.timer_label = ttk.Label(root, text="Timer : 5:00:00")

        self.voice_label = ttk.Label(root, text="Voice")
        self.voice_rule = ttk.Label(root, text="Rule")
        self.voice_question = ttk.Label(root, text="Question")
        self.voice_answer = ttk.Label(root, text="Answer")
        self.voice_hint_label = ttk.Label(root, text="Hint Label")
        self.voice_hint_button = ttk.Button(root, text="Hint")

        self.voice_node_check_label = ttk.Label(root, text="")

        self.log_text = tk.Text(root)
        self.log_button = ttk.Button(root, text="Log")

        self.start_button.grid(row=0, column=0, padx=10, pady=10)
        self.quit_button.grid(row=0, column=2, padx=10, pady=10)
        self.timer_label.grid(row=0, column=1, padx=10, pady=10)

        self.voice_label.grid(row=7, column=0, padx=10, pady=10)
        self.voice_rule.grid(row=8, column=0, padx=10, pady=10)
        self.voice_question.grid(row=9, column=0, padx=10, pady=10)
        self.voice_answer.grid(row=10, column=0, padx=10, pady=10)
        self.voice_hint_label.grid(row=11, column=1, padx=10, pady=10)
        self.voice_hint_button.grid(row=11, column=0, padx=10, pady=10)
        self.voice_node_check_label.grid(row=1, column=6, padx=10, pady=10)

        self.log_text.grid(row=8, column=6, rowspan=9, padx=10, pady=10)
        self.log_button.grid(row=7, column=6, padx=10, pady=10)

        self.voice_hint_label.grid_remove()
        self.voice_hint_button.grid_remove()

        self.log = Log(self.log_text)
        self.canInterface = CanInterface('can0', self.log)
        self.checker = Checker(self.canInterface, self.log, self.voice_node_check_label)

        self.color_node_event = threading.Event()
        self.distance_node_event = threading.Event()
        self.voice_node_event = threading.Event()

        self.voice_node = VoiceNode(self.canInterface, self.voice_question, self.voice_answer, self.voice_hint_label, self.voice_hint_button, self.log, self.voice_node_event)

        self.checker_thread = threading.Thread(target=self.checker.check_node)
        self.checker_thread.start()

    def shutdown(self):
        self.canInterface.disconnect()
        self.root.destroy()

    def start(self):
        voice_node_thread = threading.Thread(target=lambda: self.voice_node.play())
        voice_node_thread.start()
        voice_node_thread.join()

        # Ajouter le code pour les 2 autres modules

    @staticmethod
    def main():
        root = tk.Tk()
        engine = Engine(root)
        root.mainloop()

if __name__ == "__main__":
    Engine.main()
