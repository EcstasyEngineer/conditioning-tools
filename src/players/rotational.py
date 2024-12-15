# players/rotational.py
import os
import hashlib
from pydub import AudioSegment
from typing import List, Dict
from .base import Player

AUDIO_DIR = "./Audio"

def line_hash(line_text: str) -> str:
    return hashlib.md5(line_text.encode('utf-8')).hexdigest()

class RotationalPlayer(Player):
    """
    Similar to TriChamber, but conceptually for a "rotational" feel.
    Lines rotate L->C->R->L->... continuously.
    Functionally similar to TriChamber but emphasizes a sense of motion.
    """
    def play_sequence(self, line_sequence: List[Dict]) -> AudioSegment:
        final_track = AudioSegment.silent(duration=0)
        pans = [-0.5, 0.0, 0.5]  # L, C, R

        for i, line_data in enumerate(line_sequence):
            text = line_data["line"]
            h = line_hash(text)
            audio_path = os.path.join(AUDIO_DIR, f"{h}.mp3")
            if not os.path.isfile(audio_path):
                print(f"Warning: missing audio for line: {text}")
                continue

            seg = AudioSegment.from_mp3(audio_path)
            seg = seg.pan(pans[i % 3])
            # Add spacing
            final_track += seg + AudioSegment.silent(duration=500)

        return final_track
