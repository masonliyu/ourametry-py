from enum import Enum


class MomentMood(str, Enum):
    BAD = "bad"
    GOOD = "good"
    GREAT = "great"
    SAME = "same"
    WORSE = "worse"

    def __str__(self) -> str:
        return str(self.value)
