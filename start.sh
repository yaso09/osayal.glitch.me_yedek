# Setup dependencies
pip3 install -r requirements.txt
# Server development server
python3 run.py
# Serve production server
# gunicorn server:app -w --log-file server.log
