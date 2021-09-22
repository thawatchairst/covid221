web: gunicorn webCovid.wsgi 
web: python manage.py runserver 0.0.0.0:443
python manage.py collectstatic --noinput
manage.py migrate