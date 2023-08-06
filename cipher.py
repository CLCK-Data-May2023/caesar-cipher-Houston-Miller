# add your code here
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(text):
    ciphertext = ''
    shift = 5
    for character in text:
        if character in alphabet:
            position = alphabet.find(character)
            new_position = (position + shift) % 26
            new_character = alphabet[new_position]
            ciphertext += new_character
        else:
            ciphertext += character
    return ciphertext
print("Enter Text to Encrypt")
text = input()
ciphertext = encrypt(text)
print(ciphertext)
