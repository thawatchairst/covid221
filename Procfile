web: gunicorn CoreProject.wsgi --bind 127.0.0.1:$DJANGO_PORT --log-file - --log-level debug 
python manage.py collectstatic
manage.py migrate