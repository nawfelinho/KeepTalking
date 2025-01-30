import can
from Event import Event, Level

class CanInterface:
    def __init__(self, channel, log):
        try:
            self.bus = can.interface.Bus(interface='socketcan', channel=channel, bitrate=20000)
        except can.CanError as e:
            log.add(Event(what=f"Error initializing CAN interface: {e}", level=Level.ERROR))
            self.bus = None
        self.log = log

    def send(self, arbitration_id, is_extended_id, is_remote_frame):
        if self.bus is None:
            self.log.add(Event(what="CAN bus is not initialized", level=Level.ERROR))
            return
        try:
            msg = can.Message(arbitration_id=arbitration_id, is_extended_id=is_extended_id, is_remote_frame=is_remote_frame)
            self.bus.send(msg)
        except can.CanError as e:
            self.log.add(Event(what=f"Error sending CAN message: {e}", level=Level.ERROR))

    def read_can_data(self):
        if self.bus is None:
            self.log.add(Event(what="CAN bus is not initialized", level=Level.ERROR))
            return None
        try:
            msg = self.bus.recv()
            if msg is not None:
                message = {
                    'timestamp': msg.timestamp,
                    'arbitration_id': msg.arbitration_id,
                    'data': msg.data.hex()
                }
                print(message)
                return message
            else:
                return None
        except can.CanError as e:
            self.log.add(Event(what=f"Error receiving CAN message: {e}", level=Level.ERROR))
            return None

    def disconnect(self):
        if self.bus is not None:
            self.bus.shutdown()
            self.log.add(Event(what="Interface CAN déconnectée", level=Level.INFO))
