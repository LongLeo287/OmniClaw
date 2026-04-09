from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/fetch', methods=['GET'])
def fetch_data():
    url = 'https://api.example.com/data'
    headers = {
        'Authorization': f'Bearer {os.getenv("API_KEY")}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500

if __name__ == '__main__':
    app.run(debug=True)