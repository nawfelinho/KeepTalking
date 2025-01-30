import time
import can
from Event import Event, Level

class Checker:
    def __init__(self, can_interface, log, voice_node_check_label, distance_node_check_label, color_node_check_label):
        self.can_interface = can_interface
        self.log = log
        self.voice_node_check_label = voice_node_check_label
        self.distance_node_check_label = distance_node_check_label
        self.color_node_check_label = color_node_check_label

    def get_name(self, arbitration_id):
        match arbitration_id:
            case 0x730:
                return "Couleur"
            case 0x720:
                return "Vocal"
            case 0x710:
                return "Distance"
            case 0x740:
                return "Intensité"
            case _:
                return "Inconnu"

    def update(self, arbitration_id, is_connected):
        match arbitration_id:
            case 0x720:
                if is_connected:
                    self.voice_node_check_label.config(text='Noeud "Vocal" connecté', foreground="green")
                else:
                    self.voice_node_check_label.config(text='Noeud "Vocal" déconnecté', foreground="red")
                    self.log.add(Event(what="Noeud Vocal déconnecté", level=Level.ERROR))

    def check_node(self):
        ids = 0x720
        while True:
            is_connected = False
            try:
                self.can_interface.send(ids, False, True)
                self.log.add(Event(what=f'Test de la connexion sur le noeud {self.get_name(ids)}', level=Level.INFO))


                self.update(ids, is_connected)
            except can.CanError:
                self.log.add(Event(what="Le message n'a pas pu être envoyé sur le bus CAN", level=Level.ERROR))
            time.sleep(1)
