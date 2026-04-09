from flask import Flask, request, jsonify
import requests
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/fetch', methods=['POST'])
def fetch_data():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        df = pd.DataFrame(json_data)
        np_array = df.to_numpy()
        return jsonify({'data': np_array.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)