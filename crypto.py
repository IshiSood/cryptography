# Caesar Cipher
# Arguments: string, integer
# Returns: string
import string
import math

def encrypt_caesar(plaintext, offset):
    newText = []
    for i in plaintext:
        newText.append(shift_letter(i, offset))
    return "".join(newText)

#Arguments: string, string
#Returns: string
def shift_letter(letter, offset):
    alphabet = string.ascii_uppercase
    newIndex = (alphabet.find(letter) + offset)
    if newIndex > 25:
        newIndex -= 26
    return alphabet[newIndex]

#Arguments: string, string
#Returns: string
def shift_letter_back(letter, offset):
    alphabet = string.ascii_uppercase
    newIndex = (alphabet.find(letter) - offset)
    if newIndex < 0:
        newIndex += 26 
    return alphabet[newIndex]

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    newText = []
    for i in ciphertext:
        newText.append(shift_letter_back(i, offset))
    return "".join(newText)

#Arguments: string, string
#Returns: string
def get_letter_index(textChar, keyChar):
    alphabet = string.ascii_uppercase
    newIndex = alphabet.find(textChar)+alphabet.find(keyChar)
    if newIndex > 25:
        newIndex -= 26
    return alphabet[newIndex] 

#Arguments: string, string
#Returns: string
def get_ogletter_index(cipherChar, keyChar):
    alphabet = string.ascii_uppercase
    ogIndex = alphabet.find(cipherChar)-alphabet.find(keyChar)
    if ogIndex < 0:
        ogIndex = 26 + ogIndex
    return alphabet[ogIndex] 

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    newText = []
    for x in range(len(plaintext)):
        keyLetter = keyword[x % len(keyword)]
        newText.append(get_letter_index(plaintext[x], keyLetter))
    return "".join(newText)


# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    newText = []
    for x in range(len(ciphertext)):
        keyLetter = keyword[x % len(keyword)]
        newText.append(get_ogletter_index(ciphertext[x], keyLetter))
    return "".join(newText)

#Arguments: 
def bits_to_byte(tuple_bits):
    byte = 0
    for x in range(8):
        byte += tuple_bits[x] * 2**x
    return byte

#Arguments
def byte_to_bits(int_byte):
    tuple_bits = ()
    bit = int_byte
    for x in range(8):
        tuple_bits = (bit % 2,) + tuple_bits
        bit = bit // 2
    return tuple_bits

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: B - a length-n tuple of integers
def create_public_key(private_key):
    pass
    #for x in range(8):

# Arguments: string, tuple B
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, private key (W, Q, R) with W a tuple.
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    # Testing code here
    #pass
    '''print(encrypt_caesar("PYTHON", 3))
    print(decrypt_caesar("SBWKRQ", 3))
    print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
    print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))'''
    print(byte_to_bits(46))

if __name__ == '__main__':
    main()
