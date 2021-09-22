web: gunicorn CoreProject.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate