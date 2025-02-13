from enum import Enum


class LongTermResilienceLevel(str, Enum):
    ADEQUATE = "adequate"
    EXCEPTIONAL = "exceptional"
    LIMITED = "limited"
    SOLID = "solid"
    STRONG = "strong"

    def __str__(self) -> str:
        return str(self.value)
