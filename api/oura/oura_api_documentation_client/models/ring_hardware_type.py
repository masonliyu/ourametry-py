from enum import Enum


class RingHardwareType(str, Enum):
    GEN1 = "gen1"
    GEN2 = "gen2"
    GEN2M = "gen2m"
    GEN3 = "gen3"
    GEN4 = "gen4"

    def __str__(self) -> str:
        return str(self.value)
