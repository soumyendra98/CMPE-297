cd backend

python3 -m venv env

source env/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

cd frontend

npm install

npm start
