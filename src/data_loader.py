import os
import json

def load_all_lines(themes_dir: str) -> list:
    """
    Recursively load all line JSON files from the given themes directory.
    Each JSON file should contain a structure like:
    {
      "line": "i am relaxing farther and farther for Master",
      "theme": "relaxation",
      "dominant": "Master",
      "submissive": None,
      "difficulty": "light"
    }
    
    Returns:
        A list of line dictionaries loaded from all found files.
    """
    all_lines = []
    for root, dirs, files in os.walk(themes_dir):
        for f in files:
            if f.endswith(".json"):
                filepath = os.path.join(root, f)
                with open(filepath, 'r', encoding='utf-8') as jf:
                    line_data = json.load(jf)
                    # Validate structure
                    if isinstance(line_data, dict) and "line" in line_data:
                        all_lines.append(line_data)
    return all_lines
