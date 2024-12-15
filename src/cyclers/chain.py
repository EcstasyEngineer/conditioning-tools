from .base import Cycler
from typing import List, Dict

class ChainCycler(Cycler):
    """
    Cycles through lines in a fixed order repeatedly.
    """
    def __init__(self, lines: List[Dict], repeats: int = 1):
        super().__init__(lines)
        self.repeats = repeats

    def get_sequence(self) -> List[Dict]:
        return self.lines * self.repeats
