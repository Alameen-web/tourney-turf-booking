# Deploy Tourney On Railway

Railway's current Django guide recommends:

- Gunicorn as the production web server
- WhiteNoise for static files
- PostgreSQL for the production database
- GitHub repo deployment or Railway CLI deployment

This project keeps SQLite for local development, but automatically switches to Railway PostgreSQL when Railway database variables exist.

## Important Cost Note

Railway is not an unlimited free host. Its current pricing page lists a Free plan that starts with a 30-day trial and $5 credits, then changes after the trial period. Check the Railway pricing page before relying on it for long-term no-cost hosting.

## 1. Deploy From GitHub

1. Go to Railway.
2. Create a new project.
3. Choose **Deploy from GitHub repo**.
4. Select:

```text
alameenShameer/Tourney
```

Railway will detect the Django project and use `railway.json`.

## 2. Add PostgreSQL

In the Railway project canvas:

1. Click **Create**.
2. Choose **Database**.
3. Choose **Add PostgreSQL**.

## 3. Add Variables To The Web Service

Open the Django web service, then open **Variables**.

Add these variables:

```text
DJANGO_DEBUG=0
DJANGO_SECRET_KEY=replace-this-with-a-long-random-secret-key
DJANGO_ALLOWED_HOSTS=${{RAILWAY_PUBLIC_DOMAIN}}
DJANGO_CSRF_TRUSTED_ORIGINS=https://${{RAILWAY_PUBLIC_DOMAIN}}
PGDATABASE=${{Postgres.PGDATABASE}}
PGUSER=${{Postgres.PGUSER}}
PGPASSWORD=${{Postgres.PGPASSWORD}}
PGHOST=${{Postgres.PGHOST}}
PGPORT=${{Postgres.PGPORT}}
```

If your PostgreSQL service has a different name than `Postgres`, replace `Postgres` in the references with that service name.

## 4. Generate A Public Domain

Open the Django web service:

1. Go to **Settings**.
2. Open **Networking**.
3. Click **Generate Domain**.

Railway will create a domain like:

```text
your-app.up.railway.app
```

## 5. Deploy

Click **Deploy** or push a new commit to GitHub.

During deployment, Railway will run:

```bash
python manage.py migrate && python seed_data.py
```

Then it will start the app with:

```bash
python manage.py collectstatic --noinput && gunicorn turf.wsgi:application --bind 0.0.0.0:$PORT --log-file -
```

Demo logins after deployment:

```text
admin / admin123
user / user123
turf / turf123
```

## Common Fixes

If static files are missing, check the deploy logs for `collectstatic`.

If you see `DisallowedHost`, confirm:

```text
DJANGO_ALLOWED_HOSTS=${{RAILWAY_PUBLIC_DOMAIN}}
```

If forms fail with CSRF errors, confirm:

```text
DJANGO_CSRF_TRUSTED_ORIGINS=https://${{RAILWAY_PUBLIC_DOMAIN}}
```
