from datetime import datetime
from enum import Enum, auto

class Level(Enum):
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    GAMEPLAY = auto()

class Event:
    def __init__(self, date: datetime = None, what: str = "", level: Level = None):
        self.date = date if date else datetime.now()
        self.what = what
        self.level = level if level else Level.INFO

    def get_level(self):
        return self.level

    def get_string_level(self, level):
        return level.name

    def to_string(self):
        date_str = self.date.strftime("%Y-%m-%d %H:%M:%S")
        msg = f"{self.get_string_level(self.level)} : {date_str} -> {self.what}\n"
        return msg