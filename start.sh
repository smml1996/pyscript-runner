# shellcheck disable=SC1068
# pip install -r requirements.txt
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=0
python -m flask run -p 3000
