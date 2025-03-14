"""
Project Description:
1. Create a password manager GUI that allows the user to enter a website name, username, and password OR they can have a password randomly generated
2. Save the website, username, and password to a file

Completed: 3/14/2025
"""
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_creds():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    creds_to_save = f"{website} | {username} | {password}\n"

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Missing Data", message="Please be sure to fill out each field!")
    else:
        save_please = messagebox.askokcancel(title=website, message=f"These are the details entered for "
                                                            f"{website}:\nUsername: {username}\nPassword: "
                                                            f"{password}\nIs it ok to save?")
        if save_please:
            with open("data.txt", "a") as file:
                file.write(creds_to_save)
                website_input.delete(0, END)
                password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Lock image
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Email/Username label
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

# Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Website entry field
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

# Email/Username entry field
username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "shannon@gmail.com")

# Password entry field
password_input = Entry(width=19)
password_input.grid(column=1, row=3)

# Generate Password button
generate_password_button = Button(text="Generate Password", width=12, command=generate_password)
generate_password_button.grid(column=2, row=3)

# Add button
add_password_button = Button(text="Add", width=33, command=save_creds)
add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
