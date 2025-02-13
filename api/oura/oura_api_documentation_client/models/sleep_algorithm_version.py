from enum import Enum


class SleepAlgorithmVersion(str, Enum):
    V1 = "v1"
    V2 = "v2"

    def __str__(self) -> str:
        return str(self.value)
