from Event import Event, Level
import time


class Checker:
    def __init__(self, can_interface, log, color_node_check_label, voice_node_check_label, distance_node_check_label, intensite_node_check_label):
        self.can_interface = can_interface
        self.log = log
        self.color_node_check_label = color_node_check_label
        self.voice_node_check_label = voice_node_check_label
        self.distance_node_check_label = distance_node_check_label
        self.intensite_node_check_label = intensite_node_check_label

    def update(self, arbitration_id, is_connected):
        match arbitration_id:
            case 0xF30:
                if is_connected:
                    self.color_node_check_label.text = 'Noeud "Couleur" connecté'
                    self.color_node_check_label.fg = "green"
                else :
                    self.color_node_check_label.text = 'Noeud "Couleur" déconnecté'
                    self.color_node_check_label.fg = "red"
                    self.log.add(Event(what="Noeud Couleur déconnecté", level=Level.ERROR))
            case 0xF20:
                if is_connected:
                    self.voice_node_check_label.text = 'Noeud "Vocal" connecté'
                    self.voice_node_check_label.fg = "green"
                else:
                    self.voice_node_check_label.text = 'Noeud "Vocal" déconnecté'
                    self.voice_node_check_label.fg = "red"
                    self.log.add(Event(what="Noeud Vocal déconnecté", level=Level.ERROR))
            case 0xF10:
                if is_connected:
                    self.distance_node_check_label.text = 'Noeud "Distance" connecté'
                    self.distance_node_check_label.fg = "green"
                else:
                    self.distance_node_check_label.text = 'Noeud "Distance" déconnecté'
                    self.distance_node_check_label.fg = "red"
                    self.log.add(Event(what="Noeud Distance déconnecté", level=Level.ERROR))
            case 0xF40:
                if is_connected:
                    self.intensite_node_check_label.text = 'Noeud "Intensité" connecté'
                    self.intensite_node_check_label.fg = "green"
                else:
                    self.intensite_node_check_label.text = 'Noeud "Intensité" déconnecté'
                    self.intensite_node_check_label.fg = "red"
                    self.log.add(Event(what="Noeud Intensité déconnecté", level=Level.ERROR))

    def get_name(self, arbitration_id):
        match arbitration_id:
            case 0xF30:
                return "Couleur"
            case 0xF20:
                return "Vocal"
            case 0xF10:
                return "Distance"
            case 0xF40:
                return "Intensité"

    def check_node(self):
        ids = [0xF10, 0xF20, 0xF30, 0xF40]
        while True:
            for arbitration_id in ids:
                is_connected = False
                msg = self.can_interface.Message(arbitration_id=arbitration_id, is_extended_id=False, is_remote_frame=True)
                try:
                    self.can_interface.send(msg)
                    self.log.add(Event(what=f'Test de la connection sur le noeud {self.get_name(arbitration_id)}', level=Level.INFO))
                    ret = self.can_interface.read_can_data()
                    if ret['arbitration_id'] == arbitration_id:
                        is_connected = True
                    self.update(arbitration_id, is_connected)
                except self.can_interface.CanError:
                    self.log.add(Event(what="Le message n'a pas pu être envoyé sur le bus CAN", level=Level.ERROR))
            time.sleep(1)