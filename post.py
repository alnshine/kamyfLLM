from flask import Flask, request, jsonify, send_file
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
            return fail_json_receive(), 200
