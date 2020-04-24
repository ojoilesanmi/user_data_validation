from random import choice
from string import ascii_letters
import sys
user = 0

while user < 2:
    container = []
    first_name = input("Kindly enter your first name: ")

    last_name = input("Kindly enter your last name: ")

    e_mail = input("Kindly enter your email address: ")

    letters = ''.join(choice(ascii_letters) for i in range(5))

    password = first_name[0:2] + last_name[-2:] + letters

    container.extend([first_name, last_name, password])

    print("This the password generated for you {}. Are you sastisfied?".format(password))

    satisfaction = input("Press 'yes' if you are satisfied and otherwise press 'no': ")
    if satisfaction == 'yes':
        user += 1
        cl = first_name, last_name, password
        container.append(cl)
    else:
        user_password = input("Enter a password of your choice a minimum of 7 characters: ")
        if len(user_password) < 7:
            print("Password is less than 7 characters")
            client = input("Enter a password that is at least 7 characters long: ")
            if len(client) >= 7:
                user += 1
                cl = first_name, last_name, password
                container.append(cl)

        else:
            user += 1
            cl = first_name, last_name, password
            container.append(cl)

    
if user == 2:
    print(container)
    sys.exit()

