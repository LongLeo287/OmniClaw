from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    response = requests.post('https://example.com/api', json=data)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)