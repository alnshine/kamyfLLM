from flask import Flask, request
from model import *

app = Flask(__name__)

@app.route('/process_json', methods=['POST'])
def process_json():
    if request.method == "POST":
        try:
            json_data = request.json
            response_data = model(json_data)
            return response_data, 200
        except:
            data = {
            "response": {
                "retelling": "не получилось обработать сообщения",
                "time-start": "2024-03-17T08:30:45.123456789Z",
                "time-end": "2024-03-17T08:50:00.890123456Z",
                "chat-id": 0
                }
            }
            return data
