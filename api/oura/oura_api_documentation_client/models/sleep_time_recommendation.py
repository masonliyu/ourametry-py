from enum import Enum


class SleepTimeRecommendation(str, Enum):
    EARLIER_BEDTIME = "earlier_bedtime"
    EARLIER_WAKE_UP_TIME = "earlier_wake_up_time"
    FOLLOW_OPTIMAL_BEDTIME = "follow_optimal_bedtime"
    IMPROVE_EFFICIENCY = "improve_efficiency"
    LATER_BEDTIME = "later_bedtime"
    LATER_WAKE_UP_TIME = "later_wake_up_time"

    def __str__(self) -> str:
        return str(self.value)
