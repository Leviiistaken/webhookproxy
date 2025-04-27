from flask import Flask, request
import requests
import os

app = Flask(__name__)

DISCORD_WEBHOOK_URL = os.environ.get('DISCORD_WEBHOOK_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')

@app.route('/', methods=['POST'])
def proxy_webhook():
    key = request.headers.get('Authorization')
    if key != SECRET_KEY:
        return 'Unauthorized', 401

    data = request.get_json()

    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    return 'OK', response.status_code

if __name__ == "__main__":
    app.run()
