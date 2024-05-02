# loader.py
from .database import get_session
from .models import Line

def insert_into_db(template_text, real_text, subject, dominant, theme, difficulty, service, voice, audio_path):
    session = get_session()

    # validate input
    # subject should be of the form '1PS', '1PP', '2PS', '3PS'
    # difficulty should be one of 'BASIC', 'LIGHT', 'MODERATE', 'DEEP', 'EXTREME'
    # if audio file path is not none, it should be a valid path

    if not subject in ['1PS', '1PP', '2PS', '3PS']:
        raise ValueError(f"Invalid subject: {subject}")
    if not difficulty in ['BASIC', 'LIGHT', 'MODERATE', 'DEEP', 'EXTREME']:
        raise ValueError(f"Invalid difficulty level: {difficulty}")
    if audio_path is not None and not os.path.exists(audio_path):
        raise ValueError(f"Invalid audio file path: {audio_path}")

    new_line = Line(
        template_text=template_text,
        real_text=real_text,
        subject=subject,
        dominant=dominant,
        theme=theme,
        difficulty=difficulty,
        service=service,
        voice=voice,
        audio_file_path=audio_path
    )
    session.add(new_line)
    session.commit()
    session.close()