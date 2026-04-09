from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/antigravity', methods=['GET'])
def get_antigravity():
    antigravity_data = {
        'status': 'success',
        'message': 'Antigravity Manager is operational.',
        'version': '1.0.1'
    }
    return antigravity_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))