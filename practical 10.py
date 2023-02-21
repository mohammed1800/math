import numpy as np

def encode(message, key):
    message = np.array([ord(c) - ord('a') for c in message.lower()])
    message = message.reshape(-1, 1)
    encoded = np.dot(key, message) % 26
    return ''.join([chr(c + ord('a')) for c in encoded.flatten()])

def decode(encoded, key):
    encoded = np.array([ord(c) - ord('a') for c in encoded.lower()])
    encoded = encoded.reshape(-1, 1)
    decoded = np.dot(np.linalg.inv(key), encoded) % 26
    return ''.join([chr(c + ord('a')) for c in decoded.flatten()])

# Example usage
key = np.array([[3, 3], [2, 5]])
message = "attackatdawn"
encoded = encode(message, key)
print("Encoded: ", encoded)
decoded = decode(encoded, key)
print("Decoded: ", decoded)
