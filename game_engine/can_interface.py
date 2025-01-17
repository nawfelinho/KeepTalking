import can
import json
import signal
import sys

# Configurer le bus CAN
bus = can.interface.Bus(interface='socketcan', channel='can0', bitrate=20000)

def read_can_data():
    try:
        while True:
            msg = bus.recv()  # Recevoir un message CAN
            if msg is not None:
                message = {
                    'timestamp': msg.timestamp,
                    'arbitration_id': msg.arbitration_id,
                    'data': msg.data.hex()
                }
                print(json.dumps(message, indent=4))  # Afficher le message CAN au format JSON
    except KeyboardInterrupt:
        print("Interruption clavier détectée. Fermeture propre de l'interface CAN.")
    finally:
        bus.shutdown()
        print("Interface CAN fermée proprement.")

def signal_handler(sig, frame):
    print("Interruption clavier détectée. Fermeture propre de l'interface CAN.")
    bus.shutdown()
    print("Interface CAN fermée proprement.")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    read_can_data()
