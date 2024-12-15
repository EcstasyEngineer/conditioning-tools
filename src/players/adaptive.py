# players/adaptive.py
import os
import hashlib
from pydub import AudioSegment
from typing import List, Dict
from .base import Player

AUDIO_DIR = "./Audio"

def line_hash(line_text: str) -> str:
    return hashlib.md5(line_text.encode('utf-8')).hexdigest()

class AdaptivePlayer(Player):
    """
    Changes behavior based on a condition (e.g., intensity).
    If intense_mode is True, move lines toward center and boost volume.
    If false, alternate left and right with normal volume.
    """
    def __init__(self, intense_mode: bool = False):
        self.intense_mode = intense_mode

    def play_sequence(self, line_sequence: List[Dict]) -> AudioSegment:
        final_track = AudioSegment.silent(duration=0)

        if self.intense_mode:
            # All lines slightly boosted and near center
            for line_data in line_sequence:
                text = line_data["line"]
                h = line_hash(text)
                path = os.path.join(AUDIO_DIR, f"{h}.mp3")
                if not os.path.isfile(path):
                    continue
                seg = AudioSegment.from_mp3(path)
                seg = seg.pan(0.0)  # center
                seg = seg + 3       # boost by 3dB
                final_track += seg + AudioSegment.silent(duration=500)
        else:
            # Alternate left/right, normal volume
            for i, line_data in enumerate(line_sequence):
                text = line_data["line"]
                h = line_hash(text)
                path = os.path.join(AUDIO_DIR, f"{h}.mp3")
                if not os.path.isfile(path):
                    continue
                seg = AudioSegment.from_mp3(path)
                pan = -0.5 if i % 2 == 0 else 0.5
                seg = seg.pan(pan)
                final_track += seg + AudioSegment.silent(duration=500)

        return final_track
