from random import randint
from Timer import Timer
from Node import Node

class ColorNode(Node):
    def __init__(self, can_interface, color_question, color_answer, color_hint_label, color_hint_button, log, next_node_event):
        self.can_interface = can_interface
        self.color_question = color_question
        self.color_answer = color_answer
        self.color_hint_label = color_hint_label
        self.color_hint_button = color_hint_button
        self.log = log
        self.next_node_event = next_node_event

        self.colors = ['Noir', 'Blanc', 'Rouge', 'Vert clair', 'Bleu', 'Jaune', 'Magenta', 'Cyan', 'Gris', 'Bordeaux',
                  'Vert', 'Bleu marine', 'Olive', 'Prune', 'Pétrole', 'Bleu ciel', 'Lilas', 'Jaune pastel', 'Indigo',
                  'Saumon', 'Ocean digital', 'Menthe', 'Violet', 'Herbe originelle', 'Orange', 'Rose']
        self.color_codes = [
            (0, 0, 0),
            (255, 255, 255),
            (255, 0, 0),
            (144, 238, 144),
            (0, 0, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 255, 255),
            (128, 128, 128),
            (128, 0, 0),
            (0, 128, 0),
            (0, 0, 128),
            (128, 128, 0),
            (128, 0, 128),
            (0, 128, 128),
            (135, 206, 235),
            (221, 160, 221),
            (253, 253, 150),
            (75, 0, 130),
            (250, 128, 114),
            (48, 186, 143),
            (152, 255, 152),
            (148, 0, 211),
            (34, 139, 34),
            (255, 165, 0),
            (255, 192, 203)
        ]

        self.color_node_questions = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: [],
            13: [],
            14: [],
            15: [],
            16: [],
            17: [],
            18: [],
            19: [],
            20: [],
            21: [],
            22: [],
            23: [],
            24: [],
            25: [],
            26: []
        }

        self.color_node_hints = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: [],
            13: [],
            14: [],
            15: [],
            16: [],
            17: [],
            18: [],
            19: [],
            20: [],
            21: [],
            22: [],
            23: [],
            24: [],
            25: [],
            26: []
        }

        self.timer = Timer(60, "Timer module Couleur", self.log)

    def enable_hint(self):
        self.color_hint_label.grid()

    def play(self):
        color_id = randint(0, len(self.colors) - 1)
        self.color_question.config(text=self.color_node_questions[color_id])
        self.color_hint_label.config(text=self.color_node_hints[color_id])

        self.timer.start()

        answer = False
        color_m = ''
        while not answer:
            if self.timer.get_time() == 0:
                self.color_hint_button.config(command=self.enable_hint)
                self.color_hint_button.grid()

            msg = self.can_interface.read_can_data()
            if msg['arbitration_id'] == '0x030' and int(msg['data']) == color_id and color_m == color_id:
                self.color_answer.config(text=self.colors[color_id], fg=self.color_codes[color_id])
                answer = True
                self.next_node_event.set()
            else:
                if msg['arbitration_id'] == '0x030' and int(msg['data']) == color_id:
                    color_m = color_id
                self.color_answer.config(text=self.colors[int(msg['data'], 16) - 1], fg=self.color_codes[int(msg['data'], 16) - 1])
