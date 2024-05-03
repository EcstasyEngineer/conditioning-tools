import re
import sys

def load_verb_conjugations(filepath):
    verb_templates = {}
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                verb_templates[parts[0]] = parts[1]
    return verb_templates

def process_file(input_file_path, output_file_path, dominant_name):
    # Compile regex patterns with case insensitivity, assuming 1st person singular
    patterns = {
        re.compile(rf'\b{dominant_name}\b', re.IGNORECASE): '{dominant}',
        re.compile(r'\bi(\'|\’)m\b', re.IGNORECASE):   '{subject} am', # no conjuctions
        re.compile(r'\bi\b', re.IGNORECASE):   '{subject}',
        re.compile(r'\bmy\b', re.IGNORECASE):  '{subject_possessive}',
        re.compile(r'\bme\b', re.IGNORECASE):  '{subject_objective}',
        re.compile(r'\byou\b', re.IGNORECASE): '{dominant_objective}',
        re.compile(r'\bher\b', re.IGNORECASE): '{dominant_posessive}',
        re.compile(r'\bhim\b', re.IGNORECASE): '{dominant_objective}',
        re.compile(r'\bshe\b', re.IGNORECASE): '{dominant_objective}',
        re.compile(r'\bhe\b', re.IGNORECASE):  '{dominant_objective}',
        re.compile(r'\byour\b', re.IGNORECASE):'{dominant_possessive}',
        re.compile(r'\bhis\b', re.IGNORECASE): '{dominant_possessive}',
    }

    try:
        verb_templates = load_verb_conjugations('verb_conjugations.txt')

        with open(input_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                # Replace all patterns in the line {dominant}, {subject}, {subject_possessive}, etc.
                for pattern, replacement in patterns.items():
                    line = pattern.sub(replacement, line)

                # Load verb conjugation templates
                matches = re.findall(r'\{subject\}\s+(\w+)', line, re.IGNORECASE)
                for match in matches:
                    if match.lower() in verb_templates:
                        # Get the appropriate conjugation pattern [a|b]
                        pattern = r'\b' + re.escape(match) + r'\b'
                        replacement = "[" + verb_templates[match.lower()] + "]"
                        line = re.sub(pattern, replacement, line, flags=re.IGNORECASE)

                file.write(line)
        
        print(f"File processed successfully. Output saved to {output_file_path}")
    
    except FileNotFoundError:
        print("Error: The file specified does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python convert_lines.py <input_file> <output_file> <dominant_name>")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        dominant_name = sys.argv[3]
        process_file(input_file_path, output_file_path, dominant_name)


# Example usage
# python convert_lines.py input.txt output.txt "Goddess Venus"