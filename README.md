# Coco - Your Personal Voice Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-green?style=for-the-badge)

Coco is a personal voice assistant built in Python that responds to voice commands to perform tasks like playing music on YouTube, checking for Moodle assignments, and managing user profiles. It leverages speech recognition and text-to-speech technologies for a hands-free interactive experience.



---

## Features

-   **Voice-Activated Commands**: Activates on the hotword "Coco" and listens for commands.
-   **User Authentication**: Securely manages user profiles with username and password verification.
-   **Database Integration**: Stores and retrieves user credentials from a MySQL database.
-   **YouTube Integration**: Plays music or videos on YouTube based on voice commands.
-   **Moodle Integration**: Logs into a Moodle account to check for assignments.

---

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

-   Python 3.8 or newer
-   A MySQL server installed and running
-   Microsoft Edge and the corresponding `msedgedriver`

### 1. Clone the repository

First, clone the project repository to your local machine.

```bash
git clone https://github.com/MeethCodes/coco-voice-assistant.git
cd coco-voice-assistant
```

### 2. Set up the environment

It's recommended to use a virtual environment to manage project dependencies.

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate
# On Windows, use
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Install all the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

You'll need to set up a MySQL database for user management.
1. Connect to your MySQL server and create a database named coco.
2. Inside the coco database, create a table named users with the following schema:

```sql
CREATE TABLE users (
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

3. Update the database connection details (host, user, password, port) in the `cococheckdb.py`, `cocodbconnect.py`, and `cocoindb.py` files to match your MySQL configuration.

### 5. Run the Application

Once the setup is complete, you can start the voice assistant by running the `main.py` script.

```bash
python main.py
```

Say "Coco" to activate the assistant, and then provide your commands. Enjoy your new voice assistant! 🚀