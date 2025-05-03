from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

@app.route("/", methods=["POST"])
def webhook_proxy():
    auth_header = request.headers.get("Authorization")
    if auth_header != SECRET_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400

    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    return jsonify({"status": "success", "discord_response": response.text})

@app.route("/", methods=["GET"])
def home():
    return "hello there i forgot why i added that but GET OUT and yeah"

if __name__ == "__main__":
    app.run()

