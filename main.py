# Initialize lists and key
decoded_messages = []  # To store messages from partial_message.txt
decoded_int_messages = []  # To store integer-converted messages
ciphertext_hex = []  # To store ciphertexts in hex
ciphertext_ascii = []  # To store ciphertexts in ASCII
encryption_key = [-1] * 140  # To store the key

# Function to update the key based on ciphertext and message
def update_encryption_key(ciphertext, message):
    min_length = min(len(ciphertext), len(message))
    for i in range(0, min_length):
        if message[i] != 35:  # Skip characters with ASCII value 35 (i.e., '#')
            encryption_key[i] = ciphertext[i] ^ message[i]

# Function to convert hexadecimal string to ASCII integers
def hex_string_to_ascii(hex_string):
    hex_chunks = [hex_string[i:i + 2] for i in range(0, len(hex_string), 2)]
    ascii_integers = []

    for chunk in hex_chunks:
        ascii_val = int(chunk, 16)  # Convert bits to int
        ascii_integers.append(ascii_val)

    return ascii_integers

# Function to convert a string to a list of ASCII integers
def string_to_integer(message):
    ascii_list = []
    for char in message:
        ascii_val = ord(char)
        ascii_list.append(ascii_val)
    return ascii_list

# Function to check if a character is within the specified ASCII range
def is_in_range(char):
    if (32 <= char <= 90) or (97 <= char <= 122):
        return True
    else:
        return False

# Function to convert a list of ASCII integers to a string
def convert_integer_list_to_string_util(int_list):
    converted_string = ""
    for val in int_list:
        if is_in_range(val):
            converted_string += chr(val)
        else:
            converted_string += " "

    return converted_string

# Function to convert all integer lists to strings and print them
def convert_integer_list_to_string():
    for i, message in enumerate(decoded_int_messages):
        converted_string = convert_integer_list_to_string_util(message)
        print(f"Message {i + 1}: {converted_string}")

# Function to XOR a ciphertext with the key
def xor_key_with_ciphertext(index, ciphertext, key):
    min_length = min(len(ciphertext), len(key))
    for i in range(0, min_length):
        if key[i] != -1:
            xor_result = ciphertext[i] ^ key[i]
            decoded_int_messages[index][i] = xor_result

# Function to XOR the key with all ciphertexts
def xor_key_with_all_ciphertexts():
    for i in range(12):
        xor_key_with_ciphertext(i, ciphertext_ascii[i], encryption_key)

# Function to convert a list of integers to a hex string
def integer_list_to_hex(int_list):
    hex_string = ""
    for val in int_list:
        hex_code = hex(val)[2:]  # Remove '0x' prefix
        hex_string += hex_code
    return hex_string

if __name__ == '__main__':
    # Read ciphertext from file
    with open("streamciphertexts.txt", "r") as ciphertext_file:
        for line in ciphertext_file:
            ciphertext_hex.append(line.strip())

    # Close ciphertext file
    ciphertext_file.close()

    # Convert ciphertext to ASCII integers
    for hex_string in ciphertext_hex:
        ascii_integer = hex_string_to_ascii(hex_string)
        ciphertext_ascii.append(ascii_integer)

    # Read real messages from file
    with open("message.txt", "r") as message_file:
        for line in message_file:
            decoded_messages.append(line.strip())

    message_file.close()

    # Convert real messages to lists of ASCII integers
    for message in decoded_messages:
        decoded_int_messages.append(string_to_integer(message))

    # Update the key based on ciphertext and message
    for i in range(12):
        message = decoded_int_messages[i]
        ciphertext = ciphertext_ascii[i]
        update_encryption_key(ciphertext, message)

    # Perform XOR between the key and all ciphertexts
    xor_key_with_all_ciphertexts()

    # Convert the integer lists to strings and print them
    convert_integer_list_to_string()

    # Count the length of the key
    count = 0
    for i in encryption_key:
        count += 1
        if i == -1:
            break

    print(f"\nLength of the key: {count}\n")

    # Print the updated key in ASCII values
    print(f"\nUpdated key in ASCII value: {encryption_key}\n")

    # Convert the key to a hexadecimal string
    hex_key = integer_list_to_hex(encryption_key)
    print(f"\nUpdated key in hex: {hex_key}\n")

    # Write the output to FINAL_OUTPUT.txt
    with open("FINAL_OUTPUT.txt", "w") as output_file:
        for i, message in enumerate(decoded_int_messages):
            converted_string = convert_integer_list_to_string_util(message)
            output_file.write(f"Message {i + 1}: {converted_string}\n")
            
        output_file.write("\nKEY Used:\n\n")
        output_file.write(f"ASCII value: {encryption_key}\n\n")
        output_file.write(f"Hex value: {hex_key}\n")

    print("Output has been written to FINAL_OUTPUT.txt")

