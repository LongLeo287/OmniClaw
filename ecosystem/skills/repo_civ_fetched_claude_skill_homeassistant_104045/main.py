import os
from flask import Flask, request, jsonify
from homeassistant_api import HomeAssistantAPI

app = Flask(__name__)

# Initialize the Home Assistant API client
ha_api = HomeAssistantAPI(os.getenv('HOMEASSISTANT_URL'))

@app.route('/execute_command', methods=['POST'])
def execute_command():
    data = request.json
    service = data.get('service')
    entity_id = data.get('entity_id')
    attributes = data.get('attributes')
    response = ha_api.call_service(service, entity_id, **attributes)
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=8000)