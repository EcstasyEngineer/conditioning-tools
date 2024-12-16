
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

## Example Sessions

### **Somnophilia and Ego Loss Marriage**

**Description:**  
This session guides the listener into a dreamy, sleep-like state (Somnophilia), then gently erodes their sense of self (Ego Loss) while instilling a sense of union or “marriage” to the experience. By the end, the participant feels deeply merged with the hypnotic suggestions and themes of devotion.

| Phase            | Duration | Theme(s)                 | Player        | Cycler        | Script Segment?          |
|------------------|----------|--------------------------|---------------|---------------|--------------------------|
| Induction         | 2 min    | Relaxation               | Direct        | Chain         | Intro relaxation script  |
| Drift into Sleep  | 3 min    | Somnophilia + Acceptance | TriChamber    | Adaptive      | (none, mantra only)      |
| Dissolving Self   | 4 min    | Ego Loss + Confusion     | Rotational    | Cluster       | Ego-loss deepener script |
| Unified Devotion  | 3 min    | Somnophilia + Worship    | Composite     | Random        | (none, mantra only)      |
| Final Merge       | 3 min    | Ego Loss + Devotion      | Layered       | Weave         | Final marriage script    |

---

### **Latex Drone Enslavement**

**Description:**  
The subject is introduced to a scenario where they become a compliant latex-clad drone. Early phases use drone identity and obedience themes, moving into a state of total, almost mechanical servitude.

| Phase             | Duration | Theme(s)              | Player      | Cycler    | Script Segment?          |
|-------------------|----------|-----------------------|-------------|-----------|--------------------------|
| Conditioning Start | 2 min    | Submission + Drone     | Direct      | Chain     | (none, mantra only)      |
| Latex Identity     | 3 min    | Drone + Overload       | TriChamber  | Adaptive  | Latex induction script   |
| Enslavement Core   | 4 min    | Obedience + Brainwashing | Rotational | Cluster | (none, mantra only)      |
| Mechanical Reinforcement | 3 min | Drone + Mindbreak  | Composite   | Random    | Drone obedience script   |
| Final Integration  | 3 min    | Surrender + Slave      | Layered     | Weave     | (none, mantra only)      |

---

### **Productivity and Fitness Regimen**

**Description:**  
This session focuses on improving the subject’s daily productivity and encouraging a consistent fitness routine. It starts with a relaxing induction, leads into motivating suggestions, and ends with reinforcing new habits.

| Phase               | Duration | Theme(s)           | Player     | Cycler     | Script Segment?          |
|---------------------|----------|--------------------|------------|------------|--------------------------|
| Calm Focus          | 2 min    | Relaxation + Focus | Direct     | Chain      | (none, mantra only)      |
| Motivating Routine  | 3 min    | Productivity + Affirmation | TriChamber | Adaptive | Productivity script |
| Fitness Encouragement | 3 min  | Fitness + Discipline | Rotational | Cluster   | (none, mantra only)      |
| Habit Reinforcement | 4 min    | Suggestibility + Devotion | Composite | Random  | (none, mantra only)      |
| Empowered Outlook   | 3 min    | Confidence + Pride | Layered    | Weave      | Final empowerment script  |

For a more exhaustive list, [`Click Here`](Example_Sessions.md)  
For more details on the formal session grammar, [`Click Here`](Session_Grammar.md)

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

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for more information.
