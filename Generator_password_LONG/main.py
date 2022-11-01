import sys
import random
import string
import re
password=[]
characters_left=-1

def update_characters_left(number_of_charakters):
    global characters_left
    if number_of_charakters < 0 or number_of_charakters > characters_left:
        print("Liczba znaków jest spoza przedziału 0, ", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_charakters
        print("Pozostało znaków: ",characters_left )

while True:
    while True:
        password_length=input("Jak długie ma być hasło?: ")
        if not re.match(r"^[A-Za-z/]", password_length):
            break
    int_password_length=int(password_length)
    if int_password_length < 5:
        print("Hasło musi mieć minimum 5 znaków,spróbuj jeszcze raz")
    elif int_password_length>=5:
        characters_left = int_password_length
        break
while True:
    lowercase_letters=int(input("Ile małych liter ma mieć hasła?: "))
    if re.match(r"^[0-9]", str(lowercase_letters)):
        break
update_characters_left(lowercase_letters)

while True:
    uppercase_letters=int(input("Ile dużych liter ma mieć hasła?: "))
    if re.match(r"^[0-9]", str(uppercase_letters)):
        break
    else:
        print("Podaj lizcbę:")
update_characters_left(uppercase_letters)

while True:
    special_charakters=int(input("Ile znaków specjalnych ma mieć hasła?: "))
    if re.match(r"^[0-9]", str(special_charakters)):
        break

while True:
    digits=int(input("Ile cyfr ma mieć hasło?:"))
    if re.match(r"^[0-9]", str(digits)):
        break

if characters_left>0:
    print("Nie wszystkie znaki zostały wkorzystane, hasło zostanie uzupełnione małymi literami")
    lowercase_letters+=characters_left

print()
print("Długość hasła: ", password)
print("Duże litery: ", uppercase_letters)
print("Małe litery: ", lowercase_letters)
print("Znaki specialne: ", special_charakters)
print("Cyfry: ", digits)

for i in range(int_password_length):
    if lowercase_letters>0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters-=1
    if uppercase_letters>0:
        password.append((random.choice(string.ascii_uppercase)))
        uppercase_letters-=1
    if special_charakters>0:
        password.append(random.choice(string.punctuation))
        special_charakters-=1
    if digits>0:
        password.append(random.choice(string.digits))
        digits-=1
random.shuffle(password)
print("Wygenerowane hasło: ", "".join(password))

