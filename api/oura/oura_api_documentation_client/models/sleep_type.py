from enum import Enum


class SleepType(str, Enum):
    DELETED = "deleted"
    LATE_NAP = "late_nap"
    LONG_SLEEP = "long_sleep"
    REST = "rest"
    SLEEP = "sleep"

    def __str__(self) -> str:
        return str(self.value)
