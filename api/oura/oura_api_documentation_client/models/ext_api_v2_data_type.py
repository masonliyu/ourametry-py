from enum import Enum


class ExtApiV2DataType(str, Enum):
    DAILY_ACTIVITY = "daily_activity"
    DAILY_READINESS = "daily_readiness"
    DAILY_SLEEP = "daily_sleep"
    DAILY_SPO2 = "daily_spo2"
    DAILY_STRESS = "daily_stress"
    ENHANCED_TAG = "enhanced_tag"
    REST_MODE_PERIOD = "rest_mode_period"
    RING_CONFIGURATION = "ring_configuration"
    SESSION = "session"
    SLEEP = "sleep"
    SLEEP_TIME = "sleep_time"
    TAG = "tag"
    WORKOUT = "workout"

    def __str__(self) -> str:
        return str(self.value)
