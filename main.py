alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
    ciphertext = ''
    for char in plaintext:
        if char in alphabet:
            # Find the index of the character in the alphabet
            index = alphabet.index(char)
            # Shift the index by 'k' positions to the left and wrap around
            new_index = (index - k) % len(alphabet)
            # Append the corresponding character to the ciphertext
            ciphertext += alphabet[new_index]
        else:
            # If the character is not in the alphabet, leave it unchanged
            ciphertext += char
    return ciphertext

