"""
Topics Covered:
1. List comprehension
2. Dictionary comprehension
3. DataFrame comprehension

Project Description:
1. Using the NATO phonetic alphabet, return a list of the NATO words for a word that the user enters.
Ex. Shannon
['Sierra', 'Hotel', 'Alfa', 'November', 'November', 'Oscar', 'November']

Completed: 3/10/2025
UPDATED: 3/18/2025
- Added error handling (try/except/else)
"""
import pandas as pd
"""
# Original code:
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for index, row in nato_df.iterrows()}
print(nato_dict)

word = input("Enter a word: ").upper()
word_list = [nato_dict[letter] for letter in word]
print(word_list)
"""
# Updated code:
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for index, row in nato_df.iterrows()}
print(nato_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        word_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Please enter only letters of the alphabet.")
        generate_phonetic()
    else:
        print(word_list)

generate_phonetic()
