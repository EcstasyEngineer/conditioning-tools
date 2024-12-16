
# Hypnosis Content Generation Application

This project is a Python-based application designed to generate hypnosis content for use in various interfaces. It dynamically produces personalized hypnosis sessions, incorporating themes, text, images, audio, and user preferences. This document provides an overview of the project setup, usage, and development process.

## Overview

The Hypnosis Content Generation Application serves as an engine that generates dynamic and personalized hypnosis content through structured phases, each designed to guide the user deeper into a hypnotic experience. Key features include:

- **Themes**: High-level hypnosis motifs such as submission, mind emptying, or roleplay identities, which influence the content and focus of each session. [More details](Themes/Themes.md)
- **Phases**: Structured segments within each session that progress through hypnotic stages—starting with an induction, followed by deepeners, and then flowing into suggestion-focused phases based on the chosen themes. Each phase includes specific objectives, such as deepening trance, enhancing focus, or instilling particular suggestions, creating a cohesive journey for the user. [More details](src/cyclers_and_players_overview.md)
- **Sessions**: Configurations that define the hypnosis experience, including selected themes, user preferences, difficulty levels, and duration. Sessions are composed of phases, ensuring a guided and adaptive flow tailored to individual goals.
- **State Tracking**: The application constantly re-estimates the listener's arousal, focus, and depth.
  - **Arousal**: Increases if suggestive themes, or JOI state (green - increase slowly, purple increase fast). Cumulative. Plans for using heart rate data to fine tune this.
  - **Focus**: Depends on the theme (if theme calls attention), or if JOI state is in purple.
  - **Depth**: Depends on number of deepeners used recently.
- **Adaptive Content**: Based on the state tracking, the application dynamically adjusts the content to better suit the listener's current state, ensuring a more effective and personalized hypnosis experience. [More details](Adaptive_Director.md)
## User Interface
todo (mantra builder, line builder, session builder, session player)

## Use Cases


## Backend Components

- **Database**: Uses SQLite initially, with support for PostgreSQL. Stores text snippets, audio files, images, and user preferences.
- **API**: Manages session configuration and content retrieval. Supports secure data transfer and authentication.

## Getting Started
fixme  

### Prerequisites

- Python 3.8+
- Required libraries can be installed from `requirements.txt`.
- SQLite or PostgreSQL for the database.
- AWS account for Polly integration.

### Installation
fixme  

## Development

This project is designed to be modular and extendable. You can add new themes, session types, and integrations as needed.

### Directory Structure

- `app/`: Contains the main application code.
  - `api/`: API endpoints for session data retrieval.
  - `database/`: Database models and initialization scripts.
  - `discord_bot/`: Code for the Discord bot integration.
  - `static/`: Static files for the web interface.
    - `css/`: CSS stylesheets.
    - `js/`: JavaScript files.
    - `images/`: Image assets.
  - `templates/`: HTML templates for the web interface.
  - `utils/`: Utility functions and helper classes.
- `data/`: Data files for themes, text, audio, and images.
  - `preconverted/`: Input files before processing.
  - `converted/`: Processed files ready for use.
- `tests/`: Unit tests for the application.
- `run.py`: Entry point to run the application.
fixme  

### Running Tests

```bash
python -m unittest discover tests
```

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for more information.
