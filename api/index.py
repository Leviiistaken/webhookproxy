import os
from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = os.getenv("SECRET_KEY")

@app.route("/", methods=["POST"])
def proxy_webhook():
    if not WEBHOOK_URL:
        return "Webhook URL not set.", 500

    data = request.get_json()
    headers = {"Content-Type": "application/json"}
    response = requests.post(WEBHOOK_URL, json=data, headers=headers)

    return "OK", response.status_code

if __name__ == "__main__":
    app.run()
