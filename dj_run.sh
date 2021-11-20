pip3 install --upgrade virtualenv
virtualenv -p python venv
source venv/bin/activate

pip3 install -r requirements.txt
python manage.py migrate
python manage.py loaddata airline.airplane.json
python manage.py collectstatic
python manage.py test
python manage.py runserver
