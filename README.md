# Caesar_Cipher_Encryption

This Python program implements a Caesar cipher encryption function. It takes a plaintext string and a key `k` as input and returns the ciphertext where each character is shifted `k` positions to the left. It assumes that all characters are lowercase letters with no punctuation or spaces backward.

## Usage

1. Make sure you have Python installed on your system.

2. Open a Python environment or script.

3. Copy and paste the code provided into your Python environment.

4. Modify the `plaintext` and `k` variables in the example usage section to suit your needs.

5. Run the program to encrypt your plaintext using the Caesar cipher with the specified key `k`.

```python
# Example usage:
plaintext = 'hello'
k = 2
encrypted_text = encrypt(plaintext, k)
print(encrypted_text)  # Output: 'fcjjm'
