import random
import string
import re
while True:
    password_length = input("Jak długie ma być hasło?: ")
    if not re.match(r"^[A-Za-z/]", password_length):
        break
int_password_length = int(password_length)
password="".join([random.choice(string.ascii_letters+string.punctuation+string.digits) for _ in range(int_password_length)])
print(password)