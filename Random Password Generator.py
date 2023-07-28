import random
import string
def generatePassword(n):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    password = "".join(random.choice(letters+digits+symbols) for _ in range (n))
    return password
n = int(input("Enter the length of the password: "))
password = generatePassword(n)
print("Random password is:", password)