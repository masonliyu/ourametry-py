from enum import Enum


class HeartRateSource(str, Enum):
    AWAKE = "awake"
    LIVE = "live"
    REST = "rest"
    SESSION = "session"
    SLEEP = "sleep"
    WORKOUT = "workout"

    def __str__(self) -> str:
        return str(self.value)
