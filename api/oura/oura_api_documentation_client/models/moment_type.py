from enum import Enum


class MomentType(str, Enum):
    BODY_STATUS = "body_status"
    BREATHING = "breathing"
    MEDITATION = "meditation"
    NAP = "nap"
    RELAXATION = "relaxation"
    REST = "rest"

    def __str__(self) -> str:
        return str(self.value)
