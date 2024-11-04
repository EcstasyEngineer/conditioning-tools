import os
from flask import Blueprint, current_app, send_from_directory, request, jsonify
from ..database.database import get_session
from ..database.models import User, Line, Template, Theme
import uuid

api_bp = Blueprint('api', __name__)

@api_bp.route('/audio/<filename>')
def serve_audio(filename):
    audio_dir = os.path.join(current_app.root_path, '../data/audio')
    return send_from_directory(audio_dir, filename)

@api_bp.route('/api/generate_session', methods=['POST'])
def generate_session():
    data = request.get_json()

    # Extract input variables with defaults
    user_id = data.get('user_id')
    themes = data.get('themes', [])
    duration = data.get('duration', 15)
    difficulty = data.get('difficulty', 'MODERATE')
    dominant_name = data.get('dominant_name', 'Master')
    subject_name = data.get('subject_name', 'Slave')
    sub_pov = data.get('sub_pov', '1PS')
    dom_pov = data.get('dom_pov', '2PS')

    # Database session
    db_session = get_session()

    # Fetch lines based on the themes and difficulty
    lines = db_session.query(Line).join(Template).join(Theme).filter(
        Template.difficulty == difficulty,
        Theme.name.in_(themes)
    ).all()

    # Limit the number of lines based on duration (assuming 5 seconds per line)
    max_lines = (duration * 60) // 5
    selected_lines = lines[:int(max_lines)]

    # Prepare the response lines
    response_lines = []
    for line in selected_lines:
        response_lines.append({
            'text': line.real_text,
            'audio_url': line.audio_file_path,  # Adjust if necessary
            'image_url': '/static/images/default.jpg',  # Placeholder
            'display_duration': 5  # Assuming 5 seconds per line
        })

    # Get binaural audio URL based on difficulty (simplified)
    binaural_url = f'/static/audio/binaural_{difficulty.lower()}.mp3'

    # Generate a session ID
    session_id = str(uuid.uuid4())

    # Build the response
    response = {
        'session_id': session_id,
        'lines': response_lines,
        'binaural_url': binaural_url,
        'status': 'Session generated successfully.'
    }

    return jsonify(response)
