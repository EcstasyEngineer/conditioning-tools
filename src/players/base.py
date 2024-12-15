from abc import ABC, abstractmethod
from pydub import AudioSegment
from typing import List, Dict

class Player(ABC):
    """
    Abstract base class for Players.
    Players take a sequence of lines, load their audio, and produce a final AudioSegment.
    """
    @abstractmethod
    def play_sequence(self, line_sequence: List[Dict]) -> AudioSegment:
        pass
