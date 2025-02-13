from enum import Enum


class SleepTimeStatus(str, Enum):
    BAD_SLEEP_QUALITY = "bad_sleep_quality"
    NOT_ENOUGH_NIGHTS = "not_enough_nights"
    NOT_ENOUGH_RECENT_NIGHTS = "not_enough_recent_nights"
    ONLY_RECOMMENDED_FOUND = "only_recommended_found"
    OPTIMAL_FOUND = "optimal_found"

    def __str__(self) -> str:
        return str(self.value)
