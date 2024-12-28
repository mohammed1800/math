import numpy as np

def encode_message(message, matrix):

    ascii_values = [ord(char) for char in message]

    padding = len(message) % matrix.shape[0]
    if padding != 0:
        message += ' ' * (matrix.shape[0] - padding)
        ascii_values = [ord(char) for char in message]

    ascii_matrix = np.array(ascii_values).reshape(-1, matrix.shape[0]).T

    encoded_message = np.dot(matrix, ascii_matrix)
    return encoded_message

def decode_message(encoded_message, matrix):

    inverse_matrix = np.linalg.inv(matrix)

    decoded_message_matrix = np.dot(inverse_matrix, encoded_message)

    decoded_message = ''.join([chr(int(round(val))) for val in decoded_message_matrix.flatten()])
    
    return decoded_message.strip()

message = "Linear Algebra is fun"
encoding_matrix = np.array([[2, 1], [1, 3]]) 

encoded_message = encode_message(message, encoding_matrix)
print("Encoded Message (Numerical Form):")
print(encoded_message)

decoded_message = decode_message(encoded_message, encoding_matrix)
print("\nDecoded Message:")
print(decoded_message)
