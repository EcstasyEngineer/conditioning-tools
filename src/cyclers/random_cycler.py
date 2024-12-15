import random
from typing import List, Dict
from .base import Cycler

class RandomCycler(Cycler):
    def __init__(self, lines: List[Dict], num_lines: int):
        super().__init__(lines)
        self.num_lines = num_lines

    def get_sequence(self) -> List[Dict]:
        if not self.lines:
            return []
        return random.sample(self.lines, min(self.num_lines, len(self.lines)))
