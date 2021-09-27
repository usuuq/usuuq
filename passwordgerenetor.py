digits = "0123456789"
chars = "abcdefghijklmn" \
    "opqrstuvxwyz"
up = chars.upper()
special = "_!$ù?&"
all = digits+chars+special
from random import choice
password = ''.join(
    choice(all) for i in range(8)
)

print(password)
