from enum import Enum


class WorkoutIntensity(str, Enum):
    EASY = "easy"
    HARD = "hard"
    MODERATE = "moderate"

    def __str__(self) -> str:
        return str(self.value)
