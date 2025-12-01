def cipher():
        a = input("What cipher would you like to use? \n 1. Caesar \n 2. Substition \n 3. Transposition \n 4. Atbash \n")
        if a == "1":
            print(caesar())
        elif a == "2":
            print("Substitution is not out yet, please be patient.")
        elif a == "3":
            print("Transposition is not out yet, please be patient.")
        elif a == "4":
            print("Atbash is not out yet, please be patient.")
        else:
            print("That is not an option.")


def cipher_dictionary():
    definitions = {"1": "\nA caesar cipher takes your messasge and shifts it by a certain amount of spaces.\n","2": "\nA substitution cipher takes your message and converts it to the A1Z26 format. (A = 1, B = 2 etc.)\n","3": "\nA binary cipher takes your message and turns it a string of 0s and 1s.\n","4": "\nAn atbash cipher takes every letter and reverses it, so that A -> Z and B -> Y\n"}
    a = input("Which cipher would you like to know more about? \n 1. Caesar \n 2. Substitution \n 3. Binary \n 4. Atbash \n Type done in all lowercase to end this interaction")
    while a != "done":
        allowed_statements = ['1','2','3','4','done']
        if a not in allowed_statements:
            print("\nThat is not an option. Please pick a valid option or type done in all lowercase.\n")
            a = input("Which cipher would you like to know more about? \n 1. Caesar \n 2. Substitution \n 3. Binary \n 4. Atbash \n Type done in all lowercase to end this interaction \n")
        else:
            print(definitions[a])
            a = input("Which cipher would you like to know more about? \n 1. Caesar \n 2. Substitution \n 3. Binary \n 4. Atbash \n Type done in all lowercase to end this interaction \n")

def caesar():
    a = input("What message would you like to encrypt? ")
    b = int(input("How many places would you like this message to be shifted? "))
    if b > 26 or b < -26:
        b = b % 26
    encrypted = ""
    for item in a:
        if item.isalpha() == False:
            encrypted = encrypted + item
            continue
        if item == item.upper():   
            if ord(item) + b > 90:
                encrypted = encrypted + chr(65 + ord(item) + b - 91)
            else:
                encrypted = encrypted + chr(ord(item) + b)
        if item == item.lower():
            if ord(item) + b > 122:
                encrypted = encrypted + chr(97 + ord(item) + b - 123)
            else:
                encrypted = encrypted + chr(ord(item) + b)
    return encrypted

def substitution(message, key):
    pass

def binary(message):
    pass

def atbash(message):
    pass
