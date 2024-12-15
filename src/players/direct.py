from .base import Player
from pydub import AudioSegment
from typing import List, Dict
import os
import hashlib

def line_hash(line_text: str) -> str:
    return hashlib.md5(line_text.encode('utf-8')).hexdigest()

AUDIO_DIR = "./Audio"

class DirectPlayer(Player):
    def play_sequence(self, line_sequence: List[Dict]) -> AudioSegment:
        final_track = AudioSegment.silent(duration=0)
        for line_data in line_sequence:
            text = line_data["line"]
            h = line_hash(text)
            audio_path = os.path.join(AUDIO_DIR, f"{h}.mp3")
            if os.path.isfile(audio_path):
                seg = AudioSegment.from_mp3(audio_path)
                # Direct: no panning or special effects
                final_track += seg + AudioSegment.silent(duration=500)
        return final_track
