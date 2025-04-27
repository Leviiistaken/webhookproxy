from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

SECRET_KEY = os.getenv("SECRET_KEY")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

@app.route('/', methods=['POST'])
def handle_webhook():
    incoming_key = request.headers.get('Authorization')
    if incoming_key != SECRET_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    try:
        data = request.get_json()
        response = requests.post(WEBHOOK_URL, json=data)
        return jsonify({"status": "success", "discord_response": response.text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Site Aktif, bir şey yok burada."

if __name__ == '__main__':
    app.run()
