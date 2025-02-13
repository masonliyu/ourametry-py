from enum import Enum


class RingColor(str, Enum):
    BRUSHED_SILVER = "brushed_silver"
    GLOSSY_BLACK = "glossy_black"
    GLOSSY_GOLD = "glossy_gold"
    GLOSSY_WHITE = "glossy_white"
    GUCCI = "gucci"
    MATT_GOLD = "matt_gold"
    ROSE = "rose"
    SILVER = "silver"
    STEALTH_BLACK = "stealth_black"
    TITANIUM = "titanium"
    TITANIUM_AND_GOLD = "titanium_and_gold"

    def __str__(self) -> str:
        return str(self.value)
