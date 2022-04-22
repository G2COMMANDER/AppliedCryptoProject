# Stream Cipher Analysis
# Calvin Hariprasad, Cameron Ugi, Christian Moticska

import os
import sys
from os import urandom

# Step 1: Obtaining 128 bit hex plaintext

file = open(os.path.join(sys.path[0], "128BitHexCode.txt"), "r")
plaintext = file.read()
file.close()

# Step 2: Convert plaintext to decimal

i = int(plaintext, 16)
plaintext_decimal = str(i)
print(plaintext_decimal)

# Step 3: Generate 16 bit key and bitwise XOR encode


def xor_strings(s, t) -> bytes:
    """xor two strings together."""
    if isinstance(s, str):
        # Text strings contain single characters
        return b"".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        # Bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])


key_16 = urandom(16)
print("16 Bit Key:", key_16)

CipherText_16 = xor_strings(plaintext_decimal.encode('utf8'), key_16)
print("16 Bit encrypted CipherText:", CipherText_16,)

# Step 4: Generate 128 bit key (one time pad) and bitwise XOR encode

key_128 = urandom(128)  # Change this later to accomodate plaintext length
print("128 Bit Key:", key_128)

CipherText_128 = xor_strings(plaintext_decimal.encode('utf8'), key_128)
print("16 Bit encrypted CipherText:", CipherText_128,)

# Step 5: Convert Deciaml to binary


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def arrayToString(n):
    str = ''
    str = str.join(n)
    return str


CipherBin_16 = [bin(byte) for byte in bytes(CipherText_16)]
print("16 Bit encrypt to binary:", arrayToString(CipherBin_16))

CipherBin_128 = [bin(byte) for byte in bytes(CipherText_128)]
print("128 Bit encrypt to binary:", arrayToString(CipherBin_128))
# print("16 Bit encode to Binary", decimalToBinary(decimalToBinary))
# print("128 Bit encode to Binary", decimalToBinary(CipherText_128))
