from flask import Flask, request, jsonify
import asyncio
import aiosqlite

from database_helper import *

app = Flask(__name__)

init_db()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/data', methods=['POST'])
def data():
    if request.method == 'GET':
        return "invalid request type"
    json_data = request.get_json()
    location = json_data.get('location')
    timestamp = json_data.get('timestamp')
    print("")
    print("location", location)
    print("timestamp", timestamp)
    return jsonify({"data": "ok"})
    print("")



     
if __name__ == '__main__':
    app.run(debug=True)