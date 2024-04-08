# Naanmudhalvan_Jeevaregai_5025_LICET

# MusicApp

MusicApp is a web application built with Django for managing and sharing music tracks.

## Features

- Upload songs with metadata (title, artist, album, genre).
- Display a list of uploaded songs with cover images.
- Play uploaded songs directly on the web using HTML5 audio player.
- Responsive design using Bootstrap for mobile and desktop.

## Project Structure

```
musicapp/
├── musicapp/          # Django project directory
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── music/             # Django app for music-related functionality
│   ├── migrations/
│   ├── static/        # Static files (CSS, JavaScript)
│   ├── templates/     # HTML templates
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── media/             # User-uploaded media files (song audio, cover images)
├── static/            # Static files used by the project
├── db.sqlite3         # SQLite database file
├── manage.py          # Django management script
└── README.md          # Project documentation (you are here!)
```

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/musicapp.git
    ```

2. Navigate to the project directory:

    ```bash
    cd musicapp
    ```

3. Create and activate a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

4. To make migrations

    ```bash
    python manage.py makemigrations
    ```

5. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application in your web browser at http://127.0.0.1:8000/

## Usage

- Navigate to the homepage to view the list of uploaded songs.
- Click on a song title to view details including album art and audio player.
- Use the "Upload Song" button to add new songs to the collection.

## Configuration

- Database settings can be configured in `musicapp/settings.py`.
- Static files (CSS, JavaScript) are located in the `static/` directory.
- Media files (song audio, cover images) are stored in the `media/` directory.

## Dependencies

- Django
- Bootstrap
- SQLite (included with Django)
- Python
---
