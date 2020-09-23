# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    newText = []
    for i in plaintext:
        newText.append(shift_letter(i, offset))
    return "".join(newText)

def shift_letter(letter, offset):
    key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    newIndex = (key.index(letter) + offset)
    if newIndex > 25:
        newIndex -= 26
    return key[newIndex]

def shift_letter_back(letter, offset):
    key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    newIndex = (key.index(letter) - offset)
    if newIndex < 0:
        newIndex = 26 - offset
    return key[newIndex]
# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    #pass
    newText = []
    for i in ciphertext:
        newText.append(shift_letter_back(i, offset))
    return "".join(newText)

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    pass

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    # Testing code here
    #pass
    #print(encrypt_caesar("python", 3))
    print(decrypt_caesar("sbwkrq", 3))

if __name__ == '__main__':
    main()
