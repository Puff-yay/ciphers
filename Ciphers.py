def cipher():
        a = input("What cipher would you like to use? \n 1. Caesar \n 2. Substition \n 3. Transposition \n 4. Atbash \n")
        if a == "1":
            caesar()
        elif a == "2":
            substitution()
        elif a == "3":
            binary()
        elif a == "4":
            atbash()
        else:
            print("That is not an option.")


def cipher_dictionary():
    definitions = {"1": "\nA caesar cipher takes your messasge and shifts it by a certain amount of spaces.\n","2": "\nA substitution cipher takes your message and converts it to the A1Z26 format. (A = 1, B = 2 etc.)\n","3": "\nA binary cipher takes your message and turns it a string of 0s and 1s.\n","4": "\nAn atbash cipher takes every letter and reverses it, so that A -> Z and B -> Y etc.\n"}
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
        b %= 26
    encrypted = ""
    for item in a:
        if item.isalpha() == False:
            encrypted += item
            continue
        if item == item.upper():   
            if ord(item) + b > 90:
                encrypted += chr(65 + ord(item) + b - 91)
            else:
                encrypted += chr(ord(item) + b)
        if item == item.lower():
            if ord(item) + b > 122:
                encrypted += chr(97 + ord(item) + b - 123)
            else:
                encrypted += chr(ord(item) + b)
    print(encrypted)

def substitution():
    a = input("What message would you like to encrypt? ")
    encrypted = ""
    for item in a:
        if item.isalpha() == False:
            continue
        else:
            if item == item.upper():
                encrypted += str(ord(item) - 64) + " "
            else:
                encrypted += str(ord(item) - 96) + " "
    print(encrypted)

def binary():
    a = input("What message would you like to encrypt? ")
    decimal_number = None
    binary_number = ""
    encrypted = ""
    for item in a:
        decimal_number = ord(item)
        if decimal_number >= 64:
            binary_number += "1"
            decimal_number -= 64
        else:
            binary_number += "0"
        if decimal_number >= 32:
            binary_number += "1"
            decimal_number -= 32
        else:
            binary_number += "0"
        if decimal_number >= 16:
            binary_number += "1"
            decimal_number -= 16
        else:
            binary_number += "0"
        if decimal_number >= 8:
            binary_number += "1"
            decimal_number -= 8
        else:
            binary_number += "0"
        if decimal_number >= 4:
            binary_number += "1"
            decimal_number -= 4
        else:
            binary_number += "0"
        if decimal_number >= 2:
            binary_number += "1"
            decimal_number -= 2
        else:
            binary_number += "0"
        if decimal_number >= 1:
            binary_number += "1"
            decimal_number -= 1
        else:
            binary_number += "0"
        encrypted += binary_number + " "
        binary_number = ""
    print(encrypted)

def atbash():
    a = input("What message would you like to encrypt? ")
    encrypted = ""
    for item in a:
        if item.isalpha() == False:
            encrypted += item
            continue
        if item == item.upper():
            encrypted += chr(26 - (ord(item) - 64) + 65)
        else:
            encrypted += chr(26 - (ord(item) - 96) + 97)
    print(encrypted)

cipher()
