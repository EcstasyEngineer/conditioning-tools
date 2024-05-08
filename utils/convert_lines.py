import re
import sys

def load_verb_conjugations(filepath):
    verb_templates_1ps = {}
    verb_templates_1pp = {}
    verb_templates_2ps = {}
    verb_templates_3ps = {}
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            conjugations = line.strip().split('|')
            if len(conjugations) == 2: # format is "go|goes"
                verb_templates_1ps[conjugations[0]] = line.strip() # I go
                verb_templates_1pp[conjugations[1]] = line.strip() # we go
                verb_templates_2ps[conjugations[0]] = line.strip() # you go
                verb_templates_3ps[conjugations[1]] = line.strip() # she goes
            elif len(conjugations) == 4:  #format is "am|are|is|is"
                verb_templates_1ps[conjugations[0]] = line.strip() # I am
                verb_templates_1pp[conjugations[1]] = line.strip() # we are
                verb_templates_2ps[conjugations[2]] = line.strip() # you are
                verb_templates_3ps[conjugations[3]] = line.strip() # she is
    return verb_templates_1ps, verb_templates_1pp, verb_templates_2ps, verb_templates_3ps

def process_file_to_template(input_file_path, output_file_path, dominant_name, subject_name):
    # Compile regex patterns with case insensitivity, assume 1st person is subject and 2nd/3rd person is dominant
    patterns = {
        re.compile(rf'\b{subject_name}\b', re.IGNORECASE): '{subject}',  # subject name (1st person)
        re.compile(rf'\b{dominant_name}\b', re.IGNORECASE): '{dominant}',
        re.compile(r'\bi(\'|\’)m\b', re.IGNORECASE): '{subject_subjective} am', # no conjunctions
        re.compile(r'\bwe(\'|\’)re\b', re.IGNORECASE): '{subject_subjective} am', # no conjunctions (also convert to 1ps)
        re.compile(r'\bi\b', re.IGNORECASE): '{subject_subjective}',  # "I" as subjective
        re.compile(r'\bwe\b', re.IGNORECASE): '{subject_subjective}',  # "we" as subject
        re.compile(r'\bmy|mine\b', re.IGNORECASE): '{subject_possessive}',
        re.compile(r'\bme\b', re.IGNORECASE): '{subject_objective}',
        re.compile(r'\bus\b', re.IGNORECASE): '{subject_objective}',  # "us" as objective
        re.compile(r'\byou\'re\b', re.IGNORECASE): '{dominant_subjective} are',  # no conjunctions
        re.compile(r'\bthey\'re\b', re.IGNORECASE): '{dominant_subjective} are',  # no conjunctions
        re.compile(r'\byou\b', re.IGNORECASE): '{dominant_subjective}',  # warning, "you" can be subjective as well
        re.compile(r'\bshe\b', re.IGNORECASE): '{dominant_subjective}',  # "she" as subjective
        re.compile(r'\bhe\b', re.IGNORECASE): '{dominant_subjective}',  # "he" as subjective
        re.compile(r'\bhim\b', re.IGNORECASE): '{dominant_objective}',
        re.compile(r'\bthem\b', re.IGNORECASE): '{dominant_objective}',  # "them" as objective
        re.compile(r'\byour|yours\b', re.IGNORECASE): '{dominant_possessive}',
        re.compile(r'\bhis\b', re.IGNORECASE): '{dominant_possessive}',
        re.compile(r'\bher|hers\b', re.IGNORECASE): '{dominant_possessive}', # warning, "her" can be objective as well
        re.compile(r'\btheir|theirs\b', re.IGNORECASE): '{dominant_possessive}',
    }

    try:
        
        verbs_1ps,verbs_1pp,verbs_2ps,verbs_3ps = load_verb_conjugations('verb_conjugations.txt')

        with open(input_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                # Replace all patterns in the line {dominant}, {subject}, {subject_possessive}, etc.
                for pattern, replacement in patterns.items():
                    line = pattern.sub(replacement, line)

                # Load verb conjugation templates
                matches = re.findall(r'\{subject(_subjective)?\}\s+(\w+)', line, re.IGNORECASE)
                for match in matches:
                    if match.lower() in verbs_1ps:
                        # Get the appropriate conjugation pattern [a|b]
                        pattern = r'\b' + re.escape(match) + r'\b'
                        replacement = "[" + verbs_1ps[match.lower()] + "]"
                        line = re.sub(pattern, replacement, line, flags=re.IGNORECASE)
                        
                matches = re.findall(r'\{dominant(_subjective)\}\s+(\w+)', line, re.IGNORECASE)
                for match in matches:
                    if match.lower() in verbs_2ps:
                        pattern = r'\b' + re.escape(match) + r'\b'
                        replacement = "[" + verbs_2ps[match.lower()] + "]"
                        line = re.sub(pattern, replacement, line, flags=re.IGNORECASE)
                    if match.lower() in verbs_3ps:
                        pattern = r'\b' + re.escape(match) + r'\b'
                        replacement = "[" + verbs_3ps[match.lower()] + "]"
                        line = re.sub(pattern, replacement, line, flags=re.IGNORECASE)

                file.write(line)
        
        print(f"File processed successfully. Output saved to {output_file_path}")
    
    except FileNotFoundError:
        print("Error: The file specified does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python convert_lines.py <input_file> <output_file> <dominant_name> <subject_name>")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        dominant_name = sys.argv[3]
        subject_name = sys.argv[4]
        process_file_to_template(input_file_path, output_file_path, dominant_name, subject_name)


# Example usage
# python convert_lines.py input.txt output.txt "Master" "Bambi"