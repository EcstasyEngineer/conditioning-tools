import re

def template_to_text(line, subject, dominant):
    # Dictionary mappings for different grammatical persons
    subject_switch = {
        "1PS": "I",
        "1PP": "We",
        "2PS": "You",
        "3PS": "Bambi"
    }
    object_switch = {
        "1PS": "me",
        "1PP": "us",
        "2PS": "you",
        "3PS": "Bambi"
    }
    possessive_switch = {
        "1PS": "my",
        "1PP": "our",
        "2PS": "your",
        "3PS": "Bambi's"
    }

    # Replace dominant and check if placeholders exist
    replace_dominant = dominant if dominant is not None else ""
    has_dominant = "{dominant}" in line

    # Replace subjects, objects, and possessives
    replace_subject = subject_switch.get(subject, "") if subject is not None else ""
    replace_object = object_switch.get(subject, "") if subject is not None else ""
    replace_possessive = possessive_switch.get(subject, "") if subject is not None else ""

    # Regex to find verb forms like [feel|feels|feel|feels] and replace based on subject
    verb_pattern = re.compile(r'\[(\w+)\|(\w+)\|(\w+)\|(\w+)\]')
    subject_index = {"1PS": 0, "1PP": 1, "2PS": 2, "3PS": 3}
    verb_index = subject_index.get(subject, 0)

    def verb_replacer(match):
        verbs = match.group(0).strip('[]').split('|')
        return verbs[verb_index]

    line = verb_pattern.sub(verb_replacer, line)

    # Format the line with replacements
    formatted_line = line.format(subject=replace_subject, 
                                 dominant=replace_dominant,
                                 object=replace_object,
                                 possessive=replace_possessive)

    # Check for subject to determine if replacement occurred
    has_subject = any(kw in formatted_line for kw in subject_switch.values())
    
    return formatted_line, has_subject, has_dominant

# Example usage
# line_template = "{dominant}, {subject} [beg|beg|beg|begs] for the pleasure only you can provide."
# formatted_line, has_subject, has_dominant = template_to_text(line_template, "3PS", "Goddess Venus")
# print(formatted_line)
