from enum import Enum


class RingDesign(str, Enum):
    BALANCE = "balance"
    BALANCE_DIAMOND = "balance_diamond"
    HERITAGE = "heritage"
    HORIZON = "horizon"

    def __str__(self) -> str:
        return str(self.value)
