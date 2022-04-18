# Stream Cipher Analysis
# Calvin Hariprasad, Cameron Ugi, Christian Moticska

import os
import sys

# Step 1: Obtaining plaintext
file = open(os.path.join(sys.path[0], "plaintext.txt"), "r")
plaintext = file.read()

# Step 2: Convert plaintext to decimal
# plaintext_decimal = float(plaintext.txt)

# print(plaintext_decimal)
print(plaintext)

file.close()
