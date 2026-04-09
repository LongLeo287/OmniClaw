from click import command, option
click = __import__('click')
requests = __import__('requests')
cryptography = __import__('cryptography')

@command()
def fetch_data():
    """
    Fetch locomotive-scroll data from the server.
    """
    url = 'http://example.com/api/locomotive-scroll'
    response = requests.get(url)
    if response.status_code == 200:
        print('Data fetched successfully')
    else:
        click.echo(f'Failed to fetch data: {response.status_code}')

if __name__ == '__main__':
    fetch_data()