import can
from Event import Event, Level


class CanInterface:
    def __init__(self, channel, log):
        self.bus = can.interface.Bus(interface='socketcan', channel=channel, bitrate=20000)
        self.log = log

    def send(self, msg):
        self.bus.send(msg)

    def read_can_data(self):
        msg = self.bus.recv()
        if msg is not None:
            message = {
                'timestamp': msg.timestamp,
                'arbitration_id': msg.arbitration_id,
                'data': msg.data.hex()
            }
            return message

    def disconnect(self):
        self.bus.shutdown()
        self.log.add(Event(what="Interface CAN déconnectée", level=Level.INFO))
