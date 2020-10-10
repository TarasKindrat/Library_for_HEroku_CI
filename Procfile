release: python manage.py migrate
web: gunicorn library.wsgi --log-file -
heroku ps:scale web=1h