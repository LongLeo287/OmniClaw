from main import fetch_lobsters
import json

if __name__ == '__main__':
    print(json.dumps(fetch_lobsters()))