gunicorn --bind=0.0.0.0 --timeout 600 blood_group_predictor:myapp
gunicorn --bind=0.0.0.0 --timeout 600 --chdir myapp website:app
from blood_group_predictor_app.webapp import app
gunicorn --bind=0.0.0.0 --workers=4 startup:app
py -3 -m venv .env
.env\scripts\activate
pip install -r requirements.txt
$env:FLASK_APP = "blood_group_predictor.py"
python -m flask run
