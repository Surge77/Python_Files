"""
This is a more optimised and clean code of caeser cipher i.e this previos program
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower() #The lower() function in Python is a string method that converts all the characters in a string to lowercase
shift = int(input("Type the shift number:\n"))


def caeser(cipher_text,shift_amount,plain_text):
    if direction == "encode":
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount #the problem with shifting is if the alphabet start from any almost last position it shows the error of index out of range
            new_letter = alphabet[new_position]    #so to tackle this problem we again copy and paste the list i.e duplicate items in list itself we loop in the list
            cipher_text += new_letter
        print(f"Your encoded text is {cipher_text}")
    else:
        plain_text = ""
        for letter in cipher_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            plain_text += new_letter
        print(f"Your decoded text is {plain_text}")

caeser(cipher_text=text,shift_amount=shift,plain_text=text)