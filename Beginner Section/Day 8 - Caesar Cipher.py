"""
Topics Covered:
1. Functions with inputs
2. Positional vs Keyword arguments

Project Description:
1. Ask user if they want to "encode" or "decode" a message
2. Ask the user for the message itself
3. Ask the user for the amount each letter needs to be shifted in the end result
4. The code will take the user arguments and either encode or decode the provided message by shifting each letter n indices within the provided alphabet list.
   Encoding will shift the letters in a positive direction (forwards), while decoding will shift the letters in a negative direction (backwards).
   Example: encode "ab" by 2 indices == "cd"; decode "cd" by 2 indices == "ab"

Completed: 12/17/2024
"""
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")

go_again = 'yes'

while go_again == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    go_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
