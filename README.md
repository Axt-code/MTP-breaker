________________________________________________________________________
File: main.py
Description: Main decryption script.

Steps:
1. Read ciphertexts from 'streamciphertexts.txt'.
2. Convert hexadecimal ciphertexts into lists of ASCII integers.
3. Retrieve observed partial messages and convert them to ASCII integer lists.
4. Update the decryption key using XOR between ciphertexts and messages while avoiding '#' characters.
5. Check if a character's ASCII value falls within an expected range.
6. Convert ASCII integer lists to strings, replacing out-of-range characters with spaces.
7. Perform XOR between the key and ciphertexts, updating real_int_message.
8. Calculate XOR between the key and all ciphertexts.
9. Convert the key to a hexadecimal string.


#### We also have to manually change some message text by our oberservation and predict the right message so that we can get the key. after predicting we have to update message in message.txt. after few iteration we will get currect message and key  ######

Output:
- 12 decrypted messages.
- Key represented in ASCII values.
- Key length.
- Key in hexadecimal format.

- All the messages and key is written in FINAL_OUTPUT.txt

________________________________________________________________________
File: test.py
Description: Testing script for decryption.

Steps:
1. Read ciphertexts from 'streamciphertexts.txt'.
2. Convert hexadecimal ciphertexts into lists of ASCII integers.
3. Calculate XOR of all combinations of ciphertexts.
4. Populate real_message based on XOR results.
5. Utilize handle_spaces function to determine XOR consistency for spaces.
6. Update real_message and key accordingly.
7. Convert ASCII integer lists to strings.
8. Replace out-of-range characters with '#'.
9. XOR the key with individual ciphertexts and all ciphertexts, updating real_message.
10. Print the key.

- All the Partial messages is written in partial_message.txt

________________________________________________________________________
File: streamciphertexts.txt
Description: File containing 12 ciphertexts, each represented in hexadecimal format.

________________________________________________________________________
File: partial_message.txt
Description: File for storing partial decrypted messages from test.py.

________________________________________________________________________
File: FINAL_OUTPUT.txt
Description: Final output file containing the following:
1. All 12 decrypted messages.
2. The key in ASCII values.
3. The length of the key.
4. The key in hexadecimal format.
________________________________________________________________________
