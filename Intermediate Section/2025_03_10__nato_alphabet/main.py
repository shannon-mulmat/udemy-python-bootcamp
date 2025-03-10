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
"""
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for index, row in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
word_list = [nato_dict[letter] for letter in word]
print(word_list)
