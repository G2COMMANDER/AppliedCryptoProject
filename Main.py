# Stream Cipher Analysis
# Calvin Hariprasad, Cameron Ugi, Christian Moticska

import sys
import random

# Step 1: Obtaining 128 bit hex plaintext

file = open(os.path.join(sys.path[0], "128BitHexCode.txt"), "r")
plaintext = file.read()
file.close()

# Step 2: Convert plaintext to decimal

i = int(plaintext, 16)
plaintext_decimal = str(i)
print(plaintext_decimal)

# Step 3: Generate and bitwise XOR encode with a 16 bit key

key_16 =
print(key_16)
