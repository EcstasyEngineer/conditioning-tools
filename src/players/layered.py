# players/layered.py
import os
import hashlib
from pydub import AudioSegment
from typing import List, Dict
from .base import Player

AUDIO_DIR = "./Audio"

def line_hash(line_text: str) -> str:
    return hashlib.md5(line_text.encode('utf-8')).hexdigest()

class LayeredPlayer(Player):
    """
    Overlaps each subsequent line slightly over the previous one,
    creating a layered, overlapping soundscape.
    For example:
    - Start playing line 1 normally
    - After 1 second, start line 2 softly mixed in
    - After another second, start line 3, etc.

    This creates a cascade of overlapping lines.
    """
    def play_sequence(self, line_sequence: List[Dict]) -> AudioSegment:
        final_track = AudioSegment.silent(duration=0)

        # Base parameters:
        overlap_ms = 1000  # start each new line after 1 second
        volume_reduction = -5  # each overlapping line slightly quieter

        # We will build the final track iteratively
        current_start = 0
        for i, line_data in enumerate(line_sequence):
            text = line_data["line"]
            h = line_hash(text)
            path = os.path.join(AUDIO_DIR, f"{h}.mp3")
            if not os.path.isfile(path):
                continue

            seg = AudioSegment.from_mp3(path)
            # Reduce volume slightly for later lines for a "layered" feel
            seg = seg + (volume_reduction * i)

            # Overlay the current segment starting at 'current_start'
            final_track = final_track.overlay(seg, position=current_start)
            current_start += overlap_ms

        return final_track
