# Deploy Tourney On PythonAnywhere Free

PythonAnywhere is the easiest free option for this Django + SQLite project. It gives a free Beginner account one public web app at:

```text
https://YOUR_USERNAME.pythonanywhere.com/
```

## 1. Create A Free Account

Create a free Beginner account:

```text
https://www.pythonanywhere.com/
```

## 2. Clone The Project

Open a PythonAnywhere Bash console:

```bash
git clone --depth 1 https://github.com/alameenShameer/Tourney.git
cd Tourney
```

`--depth 1` keeps the clone small, which is useful on the free storage limit.

## 3. Create A Virtual Environment

Use the same Python version that you select later in the Web tab.

```bash
mkvirtualenv --python=/usr/bin/python3.10 tourney-venv
pip install -r requirements.txt
```

If Python 3.10 is not available in your account, use the newest Python version shown by PythonAnywhere and select the same version when creating the web app.

## 4. Prepare Database And Static Files

```bash
python manage.py migrate
python seed_data.py
python manage.py collectstatic --noinput
```

Demo logins after seeding:

```text
admin / admin123
user / user123
turf / turf123
```

## 5. Create The Web App

In PythonAnywhere:

1. Open the **Web** tab.
2. Click **Add a new web app**.
3. Choose **Manual configuration**.
4. Choose the same Python version used for the virtualenv.
5. Set the virtualenv path to:

```text
/home/YOUR_USERNAME/.virtualenvs/tourney-venv
```

## 6. Configure The WSGI File

Open the WSGI file from the Web tab. It will look similar to:

```text
/var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py
```

Replace its content with the code from:

```text
deployment/pythonanywhere_wsgi.py.example
```

Then replace:

```text
YOUR_USERNAME
replace-this-with-a-long-random-secret-key
```

## 7. Configure Static And Media Files

On the Web tab, add these static file mappings:

```text
URL:  /static/
Path: /home/YOUR_USERNAME/Tourney/staticfiles
```

```text
URL:  /media/
Path: /home/YOUR_USERNAME/Tourney/media
```

## 8. Reload

Click **Reload** on the PythonAnywhere Web tab.

Your site should be live at:

```text
https://YOUR_USERNAME.pythonanywhere.com/
```

Old frontend admin login:

```text
https://YOUR_USERNAME.pythonanywhere.com/admin
```

Django built-in admin:

```text
https://YOUR_USERNAME.pythonanywhere.com/django-admin/
```

## Common Fixes

If CSS or images do not load:

```bash
python manage.py collectstatic --noinput
```

Then check the `/static/` mapping and reload the web app.

If you see `DisallowedHost`, check:

```text
DJANGO_ALLOWED_HOSTS=YOUR_USERNAME.pythonanywhere.com
```

If forms fail with CSRF errors, check:

```text
DJANGO_CSRF_TRUSTED_ORIGINS=https://YOUR_USERNAME.pythonanywhere.com
```
