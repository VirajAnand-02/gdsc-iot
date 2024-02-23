from flask import Flask, request, jsonify
import asyncio
import aiosqlite

from database_helper import *

app = Flask(__name__)

init_db()
 
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/data_update', methods=['POST'])
def data_update():
    if request.method == 'GET':
        return "invalid request type", 500
    try:
        json_data = request.get_json()
        location = json_data.get('location')
        value = json_data.get('value')
    except:
        return "invalid data format"
    
    update_val(location, value)
    return jsonify({"data": "ok"})
     
@app.route('/newLocation', methods=['POST'])
def newLocation():
    if request.method == 'GET':
        return "invalid request type", 500
    try:
        json_data = request.get_json()
        location = json_data.get('location')
        timestamp = json_data.get('timestamp')
    except:
        return "invalid data format"
    
    insert_location(location, timestamp)
    print("location", location)
    print("timestamp", timestamp)
    return jsonify({"data": "ok"})




if __name__ == '__main__':
    app.run(debug=True)