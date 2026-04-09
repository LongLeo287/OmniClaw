from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def fetch_data():
    try:
        response = requests.get('http://localhost:114458')
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return 'Failed to fetch data', response.status_code
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)