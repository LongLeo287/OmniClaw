from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/fetch', methods=['GET'])
def fetch_lobsters():
    url = 'https://example.com/api/lobsters'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch lobsters'}, 500

if __name__ == '__main__':
    app.run(debug=True)