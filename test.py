# Initialize lists for ciphertexts, key, ASCII ciphertexts, XOR results, and decoded messages
cipher_data = []  # To store ciphertext data
encryption_key = [-1] * 150  # To store the encryption key
ciphertext_ascii = []  # To store ciphertexts in ASCII format
all_exor_list = []  # To store XOR results for all combinations of ciphertexts
decoded_messages = []  # To store decoded messages

# Function to convert a hexadecimal string to a list of ASCII integers
def hex_to_ascii(hex_string):
    # Split the hexadecimal string into 2-character chunks
    hex_chunks = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
    ascii_integers = []  # Initialize a list to store the ASCII integers
    
    # Iterate through each 2-character chunk
    for chunk in hex_chunks:
        # Convert the chunk to an integer in base 16 (hexadecimal)
        ascii_val = int(chunk, 16)
        ascii_integers.append(ascii_val)  # Append the ASCII integer to the list
    
    return ascii_integers  # Return the list of ASCII integers

# Function to compute the XOR of all combinations of ciphertexts
def all_exor():
    # Iterate through each ciphertext in the list
    for i in range(0, len(ciphertext_ascii)):
        exor_list = []  # Initialize a list to store XOR results for each pair of ciphertexts
        
        # Iterate through the remaining ciphertexts, forming pairs with the current ciphertext (i)
        for j in range(i + 1, len(ciphertext_ascii)):
            len_a = len(ciphertext_ascii[i])
            len_b = len(ciphertext_ascii[j])
            min_len = min(len_a, len_b)
            exor_result = []  # Initialize a list to store the XOR result for each character pair
            
            # Iterate through each character position up to the minimum length of both ciphertexts
            for k in range(min_len):
                # Compute the XOR of characters at the same position in both ciphertexts (i and j)
                exor_result.append(ciphertext_ascii[i][k] ^ ciphertext_ascii[j][k])
            
            # Append the XOR result for this pair of ciphertexts to the exor_list
            exor_list.append(exor_result)
        
        # Append the exor_list for this ciphertext to the all_exor_list
        all_exor_list.append(exor_list)

# Function to check if a character is a valid character (A-Z, a-z)
def is_valid_char(char):
    if (65 <= char <= 90) or (97 <= char <= 122):
        return True
    else:
        return False

# Function to check if a character is within the specified ASCII range (A-Z, a-z, space)
def in_range(char):
    if (65 <= char <= 90) or (97 <= char <= 122) or (char == 32):
        return True
    else:
        return False

# Function to check if a character is an uppercase letter (A-Z)
def is_capital(char):
    if (65 <= char <= 90):
        return True
    else:
        return False

# Function to handle spaces during XOR and update decoded_messages and encryption_key
def handle_spaces(i, j, k, c1, c2, cx):
    msg1 = 32  # ASCII value for space character ' '
    msg2 = (cx + 32) if is_capital(cx) else (cx - 32)
    # Determine msg2 based on whether cx is an uppercase letter
    
    # Check if either of two conditions for XOR with spaces is satisfied
    if (msg1 ^ c1) == (msg2 ^ c2):
        encryption_keyValue = msg1 ^ c1
        decoded_messages[i][k] = msg1
        decoded_messages[j][k] = msg2
        encryption_key[k] = encryption_keyValue
    elif (msg2 ^ c1) == (msg1 ^ c2):
        encryption_keyValue = msg2 ^ c1
        decoded_messages[i][k] = msg2
        decoded_messages[j][k] = msg1
        encryption_key[k] = encryption_keyValue

# Function to fill messages based on XOR results between two ciphertexts
def update_messages(i, j):
    cipher1 = ciphertext_ascii[i]        # Get the ASCII values of the first ciphertext
    cipher2 = ciphertext_ascii[j]        # Get the ASCII values of the second ciphertext
    cipher_xor = all_exor_list[i][j - i - 1]  # Get the XOR results between the two ciphertexts
    
    # Iterate through the XOR results
    for k in range(len(cipher_xor)):
        # Check if the XOR result represents a character
        if is_valid_char(cipher_xor[k]):
            # Handle spaces and update decoded_messages and encryption_key
            handle_spaces(i, j, k, cipher1[k], cipher2[k], cipher_xor[k])

# Function to convert a list of integers to a string, preserving only valid characters
def convert_to_string(int_list):
    converted_string = ""
    for i in range(0, len(int_list)):
        if in_range(int_list[i]):
            converted_string += chr(int_list[i])
        else:
            converted_string += "#"
    return converted_string

# Function to convert a list of integers to a string and print it
def print_integer_to_string():
    for i in range(0, len(decoded_messages)):
        converted_string = convert_to_string(decoded_messages[i])
        print(f"The Message {i+1} is :: " + converted_string + "\n\n")

# Function to XOR the encryption_key with a ciphertext
def xor_encryption_key_with_cipher(index, cip, encryption_key):
    minRange = min(len(cip), len(encryption_key))
    for i in range(0, minRange):
        xorRes = cip[i] ^ encryption_key[i]
        decoded_messages[index][i] = xorRes

# Function to XOR the encryption_key with all ciphertexts
def exor_encryption_key_with_all():
    for i in range(0, len(decoded_messages)):
        xor_encryption_key_with_cipher(i, encryption_key, ciphertext_ascii[i])

# Function to process messages
def process_messages():
    for i in range(len(decoded_messages)):
        for j in range(i + 1, len(decoded_messages)):
            update_messages(i, j)

if __name__ == '__main__':
    with open("streamciphertexts.txt", "r") as file:
        for line in file:
            cipher_data.append(line.strip())

    for hex_string in cipher_data:
        ascii_integer = hex_to_ascii(hex_string)
        ciphertext_ascii.append(ascii_integer)

    all_exor()

    # Fill messages with -1
    for _ in range(12):
        decoded_messages.append([-1] * 150)

    process_messages()

    # Printing message in ASCII integers
    for i in range(len(decoded_messages)):
        print(f"\nMessage {i+1} in ASCII int: {decoded_messages[i]}\n")

    print_integer_to_string()

    

    exor_encryption_key_with_all()
    
    print("\nUpdated Messages when we exore cipher with the key we got: \n\n")
    
    print_integer_to_string()

    print("\n\n")

    print(f"Updated encryption_key: {encryption_key}")
    
    with open("partial_message.txt", "w") as partial_message_file:
        for i in range(len(decoded_messages)):
            converted_string = convert_to_string(decoded_messages[i])
            partial_message_file.write(f"Message {i+1}: {converted_string}\n")

