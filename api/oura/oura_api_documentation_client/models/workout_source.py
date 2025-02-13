from enum import Enum


class WorkoutSource(str, Enum):
    AUTODETECTED = "autodetected"
    CONFIRMED = "confirmed"
    MANUAL = "manual"
    WORKOUT_HEART_RATE = "workout_heart_rate"

    def __str__(self) -> str:
        return str(self.value)
