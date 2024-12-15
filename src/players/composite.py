# players/composite.py
import os
import hashlib
from pydub import AudioSegment
from typing import List, Dict
from .base import Player

AUDIO_DIR = "./Audio"

def line_hash(line_text: str) -> str:
    return hashlib.md5(line_text.encode('utf-8')).hexdigest()

class CompositePlayer(Player):
    """
    Combines multiple sequences into one track:
    - Assume line_sequence is a combined list from multiple cyclers.
    - We'll try: first half of the sequence on the left channel,
      second half on the right channel,
      and overlay a repeated motif in center.

    In a more complex scenario, you'd pass multiple sequences separately.
    For now, we simulate by dividing the single given sequence into parts.
    """

    def play_sequence(self, line_sequence: List[Dict]) -> AudioSegment:
        if not line_sequence:
            return AudioSegment.silent(duration=0)

        # Split the sequence into two halves
        half = len(line_sequence)//2
        seq_left = line_sequence[:half]
        seq_right = line_sequence[half:]

        final_track = AudioSegment.silent(duration=0)
        
        # Build left channel track
        left_track = AudioSegment.silent(duration=0)
        for l_data in seq_left:
            text = l_data["line"]
            h = line_hash(text)
            path = os.path.join(AUDIO_DIR, f"{h}.mp3")
            if os.path.isfile(path):
                seg = AudioSegment.from_mp3(path).pan(-0.5)
                left_track += seg + AudioSegment.silent(duration=200)

        # Build right channel track
        right_track = AudioSegment.silent(duration=0)
        for r_data in seq_right:
            text = r_data["line"]
            h = line_hash(text)
            path = os.path.join(AUDIO_DIR, f"{h}.mp3")
            if os.path.isfile(path):
                seg = AudioSegment.from_mp3(path).pan(0.5)
                right_track += seg + AudioSegment.silent(duration=200)

        # Suppose we take one line from the entire sequence as a center motif
        # repeated periodically. Let's just pick the first line as a motif.
        center_track = AudioSegment.silent(duration=0)
        if line_sequence:
            motif_text = line_sequence[0]["line"]
            motif_hash = line_hash(motif_text)
            motif_path = os.path.join(AUDIO_DIR, f"{motif_hash}.mp3")
            if os.path.isfile(motif_path):
                motif_seg = AudioSegment.from_mp3(motif_path).pan(0.0).low_pass_filter(800) # filtered for subtlety
                # Repeat motif every ~5 seconds as a background loop (example)
                total_duration = max(len(left_track), len(right_track))
                repeats = total_duration // (len(motif_seg) + 3000)
                for _ in range(repeats):
                    center_track += motif_seg + AudioSegment.silent(duration=3000)

        # Combine tracks (they start at the same time; you may want offsets)
        final_track = left_track.overlay(right_track).overlay(center_track)

        return final_track
