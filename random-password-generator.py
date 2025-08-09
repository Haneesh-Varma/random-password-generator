import string
import random
length = int(input("Enter required lenght of the password: "))
charvalues = string.ascii_letters+string.digits+string.punctuation
list = []
while len(list)<length:
    randomletter = random.choice(charvalues)
    list.append(randomletter)

password = ""
for char in list:
    password += char
print(password)
