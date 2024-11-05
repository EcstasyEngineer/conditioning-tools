
# Hypnosis Content Generation Application

This project is a Python-based application designed to generate hypnosis content for use in various interfaces. It dynamically produces personalized hypnosis sessions, incorporating themes, text, images, audio, and user preferences. This document provides an overview of the project setup, usage, and development process.

## Overview

The Hypnosis Content Generation Application serves as an engine that generates dynamic and personalized hypnosis content through structured phases, each designed to guide the user deeper into a hypnotic experience. Key features include:

- **Themes**: High-level hypnosis motifs such as submission, mind emptying, or roleplay identities, which influence the content and focus of each session.
- **Phases**: Structured segments within each session that progress through hypnotic stages—starting with an induction, followed by deepeners, and then flowing into suggestion-focused phases based on the chosen themes. Each phase includes specific objectives, such as deepening trance, enhancing focus, or instilling particular suggestions, creating a cohesive journey for the user.
- **Sessions**: Configurations that define the hypnosis experience, including selected themes, user preferences, difficulty levels, and duration. Sessions are composed of phases, ensuring a guided and adaptive flow tailored to individual goals.
- **Multi-Platform Integration**: The application supports various interfaces, including web, Discord, VRChat, and local application rendering, enabling consistent and synchronized hypnosis experiences across platforms.

## Key Features

- **Web Interface**: Displays flashing words and images along with binaural beats and audio playback.
- **Discord Integration**: Provides text-only sessions through bot messages and audio sessions in shared servers.
- **VRChat Integration**: Custom VRChat world where users can experience hypnosis sessions based on pre-canned themes.
- **Local Application**: Runs similar to the web interface, with the option to render content as MP4.

## Backend Components

- **Database**: Uses SQLite initially, with support for PostgreSQL. Stores text snippets, audio files, images, and user preferences.
- **API**: Manages session configuration and content retrieval. Supports secure data transfer and authentication.

## Getting Started

### Prerequisites

- Python 3.8+
- Required libraries can be installed from `requirements.txt`.
- SQLite or PostgreSQL for the database.
- AWS account for Polly integration.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/hypnosis-content-generation-app.git
   cd hypnosis-content-generation-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Copy `.env.example` to `.env` and fill in your configuration:
     ```bash
     cp .env.example .env
     ```

4. **Initialize the database**:
   - For SQLite:
     ```bash
     python app/database/init_db.py
     ```
   - For PostgreSQL, update the `.env` with your database connection string, then run:
     ```bash
     python app/database/init_db.py
     ```

5. **Run the Application**:
   ```bash
   python run.py
   ```

## Usage

The application can be accessed through multiple interfaces:

### Web Interface

1. Open a web browser and navigate to `http://localhost:5000`.
2. Log in or create a user profile.
3. Select your preferences and start a hypnosis session.

### Discord Bot

1. Invite the bot to your Discord server.
2. Interact with the bot using commands like `!start_session`.

### VRChat

1. Join the custom VRChat world (link provided).
2. Use the in-world interface to select themes and begin a session.

### Local Application

1. Run the local renderer:
   ```bash
   python app/local_renderer.py
   ```
2. Follow the on-screen instructions to start a session.

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

### Running Tests

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for more information.
