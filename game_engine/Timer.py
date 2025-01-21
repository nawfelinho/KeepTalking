import threading
import time
from Event import Event, Level

class Timer:
    def __init__(self, duration, title, log):
        self.duration = duration
        self.remaining_time = duration
        self.title = title
        self.log = log
        self.stop_event = threading.Event()
        self.timer_thread = threading.Thread(target=self.run_timer)

    def start(self):
        self.stop_event.clear()
        self.timer_thread.start()

    def stop(self):
        self.stop_event.set()
        self.timer_thread.join()

    def get_time(self):
        return self.remaining_time

    def run_timer(self):
        while self.remaining_time > 0 and not self.stop_event.is_set():
            time.sleep(1)
            self.remaining_time -= 1
        if self.remaining_time == 0:
            self.log.add(Event(what=self.title + "terminé", level=Level.GAMEPLAY))