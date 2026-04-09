import socket

def execute(port=8000):
    """Natively checks if local network bridges are alive."""
    try:
        with socket.create_connection(('127.0.0.1', port), timeout=2):
            return f'PORT {port} ALIVE'
    except:
        return f'PORT {port} OFFLINE'
