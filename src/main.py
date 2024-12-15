from src.data_loader import load_all_lines
from src.filters import filter_lines
from src.config import AUDIO_DIR, THEMES_DIR, OUTPUT_FILE, CHOSEN_THEME, DOMINANT_WHITELIST, NUM_LINES

from src.cyclers.random_cycler import RandomCycler
from src.players.stereo_split import StereoSplitPlayer

if __name__ == "__main__":
    # Load lines
    all_lines = load_all_lines(THEMES_DIR)

    # Filter lines
    filtered_lines = filter_lines(all_lines, CHOSEN_THEME, DOMINANT_WHITELIST)

    if not filtered_lines:
        print("No lines found for the given theme and filters.")
        exit(0)

    # Use a RandomCycler
    cycler = RandomCycler(filtered_lines, NUM_LINES)
    sequence = cycler.get_sequence()

    # Use a StereoSplitPlayer
    player = StereoSplitPlayer()
    final_audio = player.play_sequence(sequence)

    final_audio.export(OUTPUT_FILE, format="mp3")
    print(f"Session exported to {OUTPUT_FILE}")
