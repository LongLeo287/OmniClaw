import requests
def fetch_locomotive_scroll_data():
    url = 'http://example.com/api/locomotive-scroll'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Failed to fetch data: {response.status_code}')