from abc import ABC, abstractmethod
from typing import List, Dict

class Cycler(ABC):
    """
    Abstract base class for Cyclers.
    Cyclers take a list of lines (dicts) and produce a sequence of lines.
    """
    def __init__(self, lines: List[Dict]):
        self.lines = lines

    @abstractmethod
    def get_sequence(self) -> List[Dict]:
        pass
