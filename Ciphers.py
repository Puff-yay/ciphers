def cipher(message):
    if isinstance(message, str) or isinstance(message, int):
        message = str(message)
        a = input("What cipher would you like to use? \n 1. Caesar \n 2. Substition \n 3. Transposition \n 4. Atbash \n")
        return a
    else:
        print("I cannot put that message through a cipher.")


def cipher_dictionary():
    definitions = {"1": "\nA caesar cipher takes your messasge and shifts it by a certain amount of spaces.\n","2": "\nA substitution cipher takes your message and converts it to the A1Z26 format. (A = 1, B = 2 etc.)\n","3": "\nA binary cipher takes your message and turns it a string of 0s and 1s.\n","4": "\nAn atbash cipher takes every letter and reverses it, so that A -> Z and B -> Y\n"}
    a = input("Which cipher would you like to know more about? \n 1. Caesar \n 2. Substitution \n 3. Binary \n 4. Atbash \n Type done in all lowercase to end this interaction")
    while a != "done":
        print(definitions[a])
        a = input("Which cipher would you like to know more about? \n 1. Caesar \n 2. Substitution \n 3. Binary \n 4. Atbash \n Type done in all lowercase to end this interaction \n")

def caesar(message, key):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_holder = ""
    if " " in message:
        message_holder = message.split(" ")


def substitution(message, key):
    pass

def binary(message):
    pass

def atbash(message):
    pass