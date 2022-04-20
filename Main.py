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
print('Key:', key_16)

CipherText = xor_strings(plaintext_decimal.encode('utf8'), key_16)
print("CipherText:", CipherText)

# Step 4: Generate 128 bit key (one time pad) and bitwise XOR encode
