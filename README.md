# AdminLTE Django Project

A Django starter project using the AdminLTE dashboard template.

This repository includes a Django application scaffold with the AdminLTE frontend assets integrated into a simple blog-style project. It is intended as a quick starting point for building admin dashboards and web apps with Django.

## Project structure

- `manage.py` — Django project management script
- `myblog/` — Django project settings and configuration
- `blog/` — application logic for the blog module
- `templates/` — project templates
- `static/` — AdminLTE static assets
- `staticfiles/` — collected static files
- `requirements.txt` — Python package requirements
- `db.sqlite3` — SQLite development database

## Requirements

- Python 3.10 or newer
- Django 5.0.x to 5.1.x
- pip

## Setup

1. Clone or download this repository.
2. Create and activate a virtual environment if needed.
3. Install the dependencies:

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

- The project is configured for modern Django versions and Python 3.10+.
- The AdminLTE assets are stored in the `static` and `staticfiles` directories.
- This repository is meant as a basic starter project for integrating a dashboard UI into a Django application.

## License

This project is provided as-is for educational and development purposes.
