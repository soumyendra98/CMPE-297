cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

FLASK_APP=main.py flask run &

cd ../frontend
npm install

npm start
