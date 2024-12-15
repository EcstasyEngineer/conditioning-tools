from .base import Cycler
from typing import List, Dict

class WeaveCycler(Cycler):
    """
    Interlace lines from two sets. Assuming self.lines is split half/half.
    """
    def get_sequence(self) -> List[Dict]:
        half = len(self.lines) // 2
        set_a = self.lines[:half]
        set_b = self.lines[half:]
        woven = []
        for a, b in zip(set_a, set_b):
            woven.extend([a, b])
        # If uneven, just append the remainder:
        if len(set_a) > len(set_b):
            woven.extend(set_a[len(set_b):])
        else:
            woven.extend(set_b[len(set_a):])
        return woven
