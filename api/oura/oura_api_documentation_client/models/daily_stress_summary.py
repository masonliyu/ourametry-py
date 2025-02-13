from enum import Enum


class DailyStressSummary(str, Enum):
    NORMAL = "normal"
    RESTORED = "restored"
    STRESSFUL = "stressful"

    def __str__(self) -> str:
        return str(self.value)
