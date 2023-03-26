import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&*()")

def gen_password():
    password_length = int(input("Enter password length: "))

    random.shuffle(characters)

    password = []

    for s in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Wanna generate a password? (Yes/No): ")
if option == "yes":
    gen_password()
elif option == "no":
    print("Program done")
    quit()
else:
    print("Invalid Input")
    quit()