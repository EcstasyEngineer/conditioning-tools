from .base import Cycler
from typing import List, Dict
import random

class RecursiveCycler(Cycler):
    """
    Picks a different cycler at runtime, simulating a higher-level meta-logic.
    For simplicity, it might randomly choose from a known list of cycler classes.
    """
    def __init__(self, lines: List[Dict], sub_cyclers: List[Cycler]):
        super().__init__(lines)
        self.sub_cyclers = sub_cyclers

    def get_sequence(self) -> List[Dict]:
        chosen_cycler = random.choice(self.sub_cyclers)
        chosen_cycler.lines = self.lines  # ensure lines are accessible
        return chosen_cycler.get_sequence()
