release: python manage.py migrate
web: daphne tictac.asgi:application --port $PORT --bind 0.0.0.0 -v2
heroku ps:scale web=1:free worker=1:free
heroku config:set DJANGO_SETTINGS_MODULE=tictac.settings --account personal
REDIS_URL: redis://h:asdfqwer1234asdf@ec2-111-1-1-1.compute-1.amazonaws.com:11