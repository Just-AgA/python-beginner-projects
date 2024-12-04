#Encrypt a text string and then decrypt it again

import random
import string

#Consider all the alphanumeric characters + the space
chars = " " + string.punctuation + string.digits + string.ascii_letters

#Make it a list and then create a copy of the list
chars = list(chars)
key = chars.copy()

#Shuffle the list copy
random.shuffle(key)

#Encryption of the input text
plain_text = input("Enter a message to encrypt: ")
cypher_text = ""

#Iterate through each letter and find its index based on the chars list,and add that value to the key list copy
for letter in plain_text:
    index = chars.index(letter)
    cypher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cypher_text}")


#Decryption of the input text
cypher_text = input("Enter a message to decrypt: ")
plain_text = ""

#Iterate through each letter in the encrypted text and find its index based on the key list,and add that value to the plain text string
for letter in cypher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {plain_text}")
print(f"Original message: {cypher_text}")

