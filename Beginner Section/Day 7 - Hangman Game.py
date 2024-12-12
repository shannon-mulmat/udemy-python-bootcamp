"""
Topics Covered:
1. Chosing random value from a list
2. User input --> variable
3. If statements
4. For loops
5. While loops

Project Description:
1. Select a random word from a list of words, example "camel"
2. Print out a string of underscores that is the same length as the chosen word, example "_ _ _ _ _"
3. Ask the user to guess a letter, if that letter is in the word then update the string of underscores with the guessed letter in the correct position. 
   If the guess is wrong, the user loses a life. Either way, they are asked to guess another letter. Example "c _ _ _ _", "c _ _ e _", "c _ m e _", etc.
4. If the user guesses all letters in the word before they lose all their lives, they win! Otherwuse, they lose.

Completed: 12/12/2024
"""
import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
    print(f"**************************** YOU HAVE {lives} LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word and guess not in guessed_letters:
        lives -= 1
        print(f"You guessed '{guess}', that letter is not in the word. You lose a life.")
    elif guess not in chosen_word and guess in guessed_letters:
        print(f"You've already guessed the letter '{guess}', you will not lose a life for that.")
    elif guess in chosen_word and guess in guessed_letters:
        print(f"You've already guessed the letter '{guess}'.")

    if lives == 0:
        game_over = True
        print(f"*********************** The word was {chosen_word} - YOU LOSE **********************")

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    print(stages[lives])

    guessed_letters.append(guess)
