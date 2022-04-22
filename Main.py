# XOR Encryption Algorithm - www.101computing.net/xor-encryption-algorithm/
import os
import sys


def binary(num, length=8):
    b = bin(num).lstrip("0b")
    b = "0" * (length-len(b)) + b
    return b


def xorEncrypt(key):
    keyLength = len(key)
    cipherBin = ""

    for i in range(0, len(plaintext)):
        j = i % keyLength
        xor = ord(plaintext[i]) ^ ord(key[j])
        cipherBin = cipherBin + binary(xor)

    return cipherBin


file = open(os.path.join(sys.path[0], "128BitHexCode.txt"), "r")
plaintext = file.read()
file.close()

key_16 = "WoRd"
key_128 = "C&F)J@NcRfUjXn2r"

print("16 Bit Cipher: ", xorEncrypt(key_16))
print("The 16 bit Cipher has:", xorEncrypt(key_16).count("1"), "1s")
print("128 Bit Cipher:", xorEncrypt(key_128))

# Count the number of 1s
# Subtrarct the two counts
# Repeat over a large number of sets
