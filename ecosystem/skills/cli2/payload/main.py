import os
from CIV_FETCHED_cli2_123057 import fetch_data, process_data

# UPGRADE existing system logic here
if __name__ == '__main__':
    data = fetch_data()
    processed_data = process_data(data)
    print(processed_data)