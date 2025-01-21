import threading
import tkinter as tk
from tkinter import ttk

from CanInterface import CanInterface
from Checker import Checker
from ColorNode import ColorNode
from DistanceNode import DistanceNode
from VoiceNode import VoiceNode
from Log import Log
from Timer import Timer

def shutdown():
    canInterface.disconnect()
    root.destroy()

def start():
    global colorNode
    global distanceNode
    global voiceNode

    # TODO : affichage du timer
    global_timer = Timer(300, "Timer général", log, timer_label)

    color_node_event = threading.Event()
    color_node_thread = threading.Thread(target=lambda: colorNode.play())
    color_node_thread.start()
    color_node_event.wait()

    distance_node_event = threading.Event()
    distance_node_thread = threading.Thread(target=lambda: distanceNode.play())
    distance_node_thread.start()
    distance_node_event.wait()

    voice_node_thread = threading.Thread(target=lambda: voiceNode.play())
    voice_node_thread.start()

root = tk.Tk()
root.geometry("1366x900")

start_button = ttk.Button(root, text="Start", command=start)
quit_button = ttk.Button(root, text="Quit", command=shutdown)
timer_label = ttk.Label(root, text="Timer : 5:00:00")

color_label = ttk.Label(root, text="Color")
color_rule = ttk.Label(root, text="")
color_question = ttk.Label(root, text="")
color_answer = ttk.Label(root, text="")
color_hint_label = ttk.Label(root, text="")
color_hint_button = ttk.Button(root, text="Hint")

voice_label = ttk.Label(root, text="Voice")
voice_rule = ttk.Label(root, text="Rule")
voice_question = ttk.Label(root, text="Question")
voice_answer = ttk.Label(root, text="Answer")
voice_hint_label = ttk.Label(root, text="Hint Label")
voice_hint_button = ttk.Button(root, text="Hint")

distance_label = ttk.Label(root, text="Distance")
distance_rule = ttk.Label(root, text="Rule")
distance_question = ttk.Label(root, text="Question")
distance_answer = ttk.Label(root, text="Answer")
distance_hint_label = ttk.Label(root, text="Hint Label")
distance_hint_button = ttk.Button(root, text="Hint")

color_node_check_label = ttk.Label(root, text="")
voice_node_check_label = ttk.Label(root, text="")
distance_node_check_label = ttk.Label(root, text="")
intensite_node_check_label = ttk.Label(root, text="")

log_text = tk.Text(root)
log_button = ttk.Button(root, text="Log")

start_button.grid(row=0, column=0, padx=10, pady=10)
quit_button.grid(row=0, column=2, padx=10, pady=10)
timer_label.grid(row=0, column=1, padx=10, pady=10)

color_label.grid(row=1, column=0, padx=10, pady=10)
color_rule.grid(row=2, column=0, padx=10, pady=10)
color_question.grid(row=3, column=0, padx=10, pady=10)
color_answer.grid(row=5, column=0, padx=10, pady=10)
color_hint_label.grid(row=6, column=1, padx=10, pady=10)
color_hint_button.grid(row=6, column=0, padx=10, pady=10)
color_node_check_label.grid(row=0, column=6, padx=10, pady=10)

voice_label.grid(row=7, column=0, padx=10, pady=10)
voice_rule.grid(row=8, column=0, padx=10, pady=10)
voice_question.grid(row=9, column=0, padx=10, pady=10)
voice_answer.grid(row=10, column=0, padx=10, pady=10)
voice_hint_label.grid(row=11, column=1, padx=10, pady=10)
voice_hint_button.grid(row=11, column=0, padx=10, pady=10)
voice_node_check_label.grid(row=1, column=6, padx=10, pady=10)

distance_label.grid(row=13, column=0, padx=10, pady=10)
distance_rule.grid(row=14, column=0, padx=10, pady=10)
distance_question.grid(row=15, column=0, padx=10, pady=10)
distance_answer.grid(row=16, column=0, padx=10, pady=10)
distance_hint_label.grid(row=17, column=1, padx=10, pady=10)
distance_hint_button.grid(row=17, column=0, padx=10, pady=10)
distance_node_check_label.grid(row=3, column=6, padx=10, pady=10)

intensite_node_check_label.grid(row=4, column=6, padx=10, pady=10)

log_text.grid(row=8, column=6, rowspan=9, padx=10, pady=10)
log_button.grid(row=7, column=6, padx=10, pady=10)

color_hint_label.grid_remove()
color_hint_button.grid_remove()
voice_hint_label.grid_remove()
voice_hint_button.grid_remove()
distance_hint_label.grid_remove()
distance_hint_button.grid_remove()

log = Log(log_text)
canInterface = CanInterface('can0', log)
checker = Checker(canInterface, log, color_node_check_label, voice_node_check_label, distance_node_check_label, intensite_node_check_label)

color_node_event = threading.Event()
distance_node_event = threading.Event()

colorNode = ColorNode(canInterface, color_question, color_answer, color_hint_label, color_hint_button, log, color_node_event)
distanceNode = DistanceNode(canInterface, distance_question, distance_answer, distance_hint_label, distance_hint_button, log, distance_node_event)
voiceNode = VoiceNode(canInterface, voice_question, voice_answer, voice_hint_label, voice_hint_button, log)

checker_thread = threading.Thread(target=checker.check_node)
checker_thread.start()

root.mainloop()