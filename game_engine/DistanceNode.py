from Timer import Timer
from random import randint

class DistanceNode:
    def __init__(self, can_interface, distance_question, distance_answer, distance_hint_label, distance_hint_button, log, next_node_event):
        self.can_interface = can_interface
        self.distance_question = distance_question
        self.distance_answer = distance_answer
        self.distance_hint_label = distance_hint_label
        self.distance_hint_button = distance_hint_button
        self.log = log
        self.next_node_event = next_node_event

        self.timer = Timer(60, "Timer module Distance", self.log)

    def enable_hint(self):
        self.distance_hint_label.grid()

    def play(self):
        distance = randint(30, 150)

        self.distance_question.config(text="Trouvez la bonne distance")
        self.distance_answer.config(text="")

        answer = False
        while not answer:
            if self.timer.get_time() == 0:
                self.distance_hint_button.config(command=self.enable_hint)
                self.distance_hint_button.grid()

            msg = self.can_interface.read_can_data()
            if msg and msg['arbitration_id'] == '0x010':
                answer = int(msg['data'], 16) - 1
                if answer == distance:
                    self.distance_answer.config(text=str(distance), fg="green")
                    answer = True
                else:
                    self.distance_answer.config(text=str(distance) + "la distance cherchée est inférieure") if answer > distance else self.distance_hint_label.config(text=str(distance) + "la distance cherchée est supérieure")
                    self.distance_hint_label.config(text=f"la distance cherchée se trouve entre {distance - randint(3, 7)} et {distance + randint(3, 7)}")