# Stream Cipher Analysis
# Calvin Hariprasad, Cameron Ugi, Christian Moticska
import random
import string


def binary(num, length=8):
    b = bin(num).lstrip("0b")
    b = "0" * (length-len(b)) + b
    return b


def generateKey(n):  # Generates "x" bit password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(n))
    return password


def xorEncrypt(key):  # encrypts the plaintext with the "x" bit key
    keyLength = len(key)
    cipherBin = ""

    for i in range(0, len(plaintext)):
        j = i % keyLength
        xor = ord(plaintext[i]) ^ ord(key[j])
        cipherBin = cipherBin + binary(xor)

    return cipherBin


counter = 0

# Repeat over a large number of sets
for i in range(1000):
    plaintext = generateKey(16)
    print("Plaintext:", plaintext)
    pass_16 = generateKey(4)
    print("16 bit key: ", pass_16)
    pass_128 = generateKey(16)
    print("128 bit key:", pass_128)

    # Output the ciphertext in binary and count the number of 1s
    key_16 = xorEncrypt(pass_16)
    print("\n16 Bit Cipher: ", key_16)
    print("The 16 bit Cipher has: ", key_16.count("1"), "1s")

    # encrypts
    key_128 = xorEncrypt(pass_128)
    print("128 Bit Cipher:", key_128)
    print("The 128 bit Cipher has:", key_128.count("1"), "1s")
    key_128 = xorEncrypt(pass_128)

    # Subtrarct the two counts
    difference = key_16.count("1") - key_128.count("1")
    print("\n16 bit - 128 bit encryption:", difference)

    counter += difference

print(counter/1000)
