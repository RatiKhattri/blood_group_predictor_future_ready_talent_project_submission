gunicorn --bind=0.0.0.0 --timeout 600 blood_group_predictor:myapp
gunicorn --bind=0.0.0.0 --timeout 600 --chdir myapp website:app
from blood_group_predictor_app.webapp import app
gunicorn --bind=0.0.0.0 --workers=4 startup:app
