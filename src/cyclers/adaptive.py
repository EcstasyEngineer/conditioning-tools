from .base import Cycler
from typing import List, Dict

class AdaptiveCycler(Cycler):
    """
    Adapt based on some condition (e.g., time or user feedback).
    For now, just picks half the lines if 'adapting'.
    """
    def __init__(self, lines: List[Dict], adapt: bool = False):
        super().__init__(lines)
        self.adapt = adapt

    def get_sequence(self) -> List[Dict]:
        if self.adapt:
            half = len(self.lines)//2
            return self.lines[:half]
        else:
            return self.lines
