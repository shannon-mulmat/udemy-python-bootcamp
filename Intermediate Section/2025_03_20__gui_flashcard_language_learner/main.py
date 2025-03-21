"""
Project Description:
- Create a flashcard app for learning words in another language

Completed: 3/21/2025
"""
from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_card = {}
data_dict = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
    language_to_learn = original_data.columns.values[0]
    native_language = original_data.columns.values[1]
else:
    data_dict = data.to_dict(orient="records")
    language_to_learn = data.columns.values[0]
    native_language = data.columns.values[1]

# ------------------------------------ Go to the next card when unknown ------------------------------------ #
def next_card():
    global language_to_learn, current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    word_to_learn = current_card[language_to_learn]

    canvas.itemconfig(language_text, text=language_to_learn, fill="black")
    canvas.itemconfig(word_text, text=word_to_learn, fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)

    flip_timer = window.after(3000, func=flip_to_translation)
# ------------------------------------ Show translation of word ------------------------------------ #
def flip_to_translation():
    global native_language
    native_language_word = current_card[native_language]

    canvas.itemconfig(language_text, text=native_language, fill="white")
    canvas.itemconfig(word_text, text=native_language_word, fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)
# ------------------------------------ Go to the next card and remove known card from deck ------------------------------------ #
def is_known():
    data_dict.remove(current_card)
    data = pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
# ------------------------------------ UI Setup ------------------------------------ #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_to_translation)

# Flashcard canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# "Wrong" button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

# "Right" button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
