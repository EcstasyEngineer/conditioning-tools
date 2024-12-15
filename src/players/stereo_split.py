from .base import Player
from pydub import AudioSegment
from typing import List, Dict
import os, hashlib

AUDIO_DIR = "./Audio"

def line_hash(line_text: str) -> str:
    return hashlib.md5(line_text.encode('utf-8')).hexdigest()

class StereoSplitPlayer(Player):
    """
    Alternate lines between left and right channels.
    line 1: left, line 2: right, line 3: left, etc.
    """
    def play_sequence(self, line_sequence: List[Dict]) -> AudioSegment:
        final_track = AudioSegment.silent(duration=0)
        for i, line_data in enumerate(line_sequence):
            text = line_data["line"]
            h = line_hash(text)
            audio_path = os.path.join(AUDIO_DIR, f"{h}.mp3")
            if os.path.isfile(audio_path):
                seg = AudioSegment.from_mp3(audio_path)
                # Even index: left (-0.5 pan), odd index: right (+0.5 pan)
                pan = -0.5 if i % 2 == 0 else 0.5
                seg = seg.pan(pan)
                final_track += seg + AudioSegment.silent(duration=500)
        return final_track
