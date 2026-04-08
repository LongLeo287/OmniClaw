from flask import Flask, request
from pymongo import MongoClient
import os

app = Flask(__name__)
client = MongoClient(os.getenv('MONGO_URI'))
db = client[os.getenv('DATABASE')]
collections = [col for col in db.list_collection_names() if col not in ['system', 'admin']]

@app.route('/fetch', methods=['GET'])
def fetch_data():
    collection_name = request.args.get('collection')
    if collection_name in collections:
        data = list(db[collection_name].find())
        return {'data': data}
    else:
        return {'error': 'Collection not found'}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)