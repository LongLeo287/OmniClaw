import zlib
import json
def compress_data(data):
    # Compress the data using zlib
    compressed_data = zlib.compress(json.dumps(data).encode())
    return compressed_data
def decompress_data(compressed_data):
    # Decompress the data using zlib
    decompressed_data = zlib.decompress(compressed_data)
    return json.loads(decompressed_data.decode())