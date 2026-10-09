# AdminLTE Django Project

Initial setup for AdminLTE using Python 2.7 and Django 1.9.

This repository contains a Django project that integrates the AdminLTE dashboard template with a simple blog-style application. It is intended as a starter project for building admin dashboards and web apps with Django.

## Project structure

- `manage.py` — Django project management script
- `myblog/` — project settings and application configuration
- `blog/` — blog app code
- `templates/` — HTML templates used by the project
- `static/` — static assets for the AdminLTE theme
- `staticfiles/` — collected static files
- `requirements.txt` — Python dependency list
- `db.sqlite3` — SQLite database file

## Prerequisites

- Python 2.7
- Django 1.9
- pip

## Setup

1. Create a Django project named `myblog` if you are starting from scratch.
2. Clone or download this repository into your project directory.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open the application in your browser:

   ```text
   http://127.0.0.1:8000/
   ```

## Notes

- This project is configured for Python 2.7 and Django 1.9.
- AdminLTE assets are included under the `static` and `staticfiles` directories.
- The repository is meant as a basic starter layout for integrating a dashboard UI into a Django application.

## License

This project is distributed as-is for educational and development purposes.
