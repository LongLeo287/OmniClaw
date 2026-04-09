from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/v1/gitingest', methods=['POST'])
def gitingest_extension():
    data = request.json
    repo_url = data.get('repo_url')
    branch = data.get('branch', 'main')
    
    # Placeholder for actual git operations
    result = {'status': 'success', 'message': f'Repo URL: {repo_url}, Branch: {branch}'}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)