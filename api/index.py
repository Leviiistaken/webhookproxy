# main.py
from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1333804650788556873/qcNfHcfm3WV1VbREA_fDZ2AJ0bUm3W8s6DGhDEQ3NIQxCgQJlyaOIc2pvjNarJTpkJ8O"

@app.route('/', methods=['POST'])
def forward():
    data = request.get_json()
    headers = {'Content-Type': 'application/json'}
    
    # Discord webhooka POST atıyoruz
    response = requests.post(WEBHOOK_URL, json=data, headers=headers)
    
    return {'status': 'ok', 'discord_response_code': response.status_code}

@app.route('/', methods=['GET'])
def home():
    return "Hello, nothing to see here."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
