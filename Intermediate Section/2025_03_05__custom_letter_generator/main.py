"""
Topics Covered:
1. Reading files
2. Writing files
3. Using str.strip() to clean strings

Project Description:
1. Create a letter using starting_letter.txt for each name in invited_names.txt
2. Replace the [name] placeholder with the actual name.
3. Save the letters in the folder "ReadyToSend".

Completed: 3/5/2025
"""
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names_list:
        cleaned_name = name.strip('\n')
        new_letter = letter_contents.replace(PLACEHOLDER, cleaned_name)
        with open(f"./Output/ReadyToSend/letter_for_{cleaned_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)
