# Tourney

Tourney is a small Django turf booking project. It keeps the core workflow only:

- users register and log in
- turf owners register their turf
- admins approve turf registrations
- users browse approved turfs and request bookings
- turf owners approve or cancel booking requests
- users can view booking history

## Tech Stack

- Python
- Django
- SQLite

XAMPP and MySQL are not required for the current version.

## Setup

```bash
cd turffinal
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python seed_data.py
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Demo Accounts

| Role | Username | Password |
| --- | --- | --- |
| Admin | `admin` | `admin123` |
| User | `user` | `user123` |
| Turf owner | `turf` | `turf123` |

## Useful URLs

- `/` - home page
- `/turfs/` - turf listing
- `/login/` - login
- `/register/user/` - user registration
- `/register/turf/` - turf owner registration
- `/site-admin/` - simple project admin dashboard
- `/django-admin/` - Django's built-in admin

## Project Structure

```text
turffinal/
  manage.py
  seed_data.py
  requirements.txt
  turf/
    settings.py
    urls.py
  tapp/
    models.py
    forms.py
    urls.py
    views/core.py
    templates/
    static/tapp/site.css
```

## Refactor Notes

The project was simplified from a mixed older codebase. Removed pieces include shop/club routes, mobile API stubs, rent item imports, duplicate booking URLs, large unused frontend templates, and copied vendor static folders.

## Free Deployment

Use PythonAnywhere for a true no-cost Django deployment. Railway is also configured, but its free tier is credit-based and better for trials or demos.

See these guides:

```text
deployment/pythonanywhere.md
deployment/railway.md
```
