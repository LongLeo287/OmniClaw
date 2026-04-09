from mempalace import MemPalaceClient
from django.conf import settings
import os

# Initialize the MemPalace client with API key and endpoint
client = MemPalaceClient(api_key=os.getenv('MEMPALACE_API_KEY'), endpoint='https://api.mempalace.com')

def process_chat(chat_data):
    # Process chat data using MemPalace's semantic search capabilities
    response = client.search(query=chat_data['query'], context=chat_data.get('context'))
    return response