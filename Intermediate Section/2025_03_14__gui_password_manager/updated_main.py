"""
Topics Covered:
1. Error handling with try/except/else/finally keywords
2. JSON load(), dump(), update()

Project Description:
1. Update the password manager program to save to a JSON file instead of a text file
2. Add error handling to the save_creds() function
3. Allow a user to seach their saved credentials for a specific website, and make the website/username/password pop up in a
   message box if there is an entry in the JSON file for the website provided

Completed: 3/18/2025
"""
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
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
    creds_to_save = {
        website: {
            "username": username,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Missing Data", message="Please be sure to fill out each field!")
    else:
        save_please = messagebox.askokcancel(title=website, message=f"These are the details entered for "
                                                            f"{website}:\nUsername: {username}\nPassword: "
                                                            f"{password}\nIs it ok to save?")
        if save_please:
            try:
                with open("data.json", "r") as file:
                    # Read the old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    # Saving the updated data
                    json.dump(creds_to_save, file, indent=4)
            else:
                # Updating the old data with new data (add a new entry to the existing dictionary)
                # Only runs if the try block works
                data.update(creds_to_save)

                with open("data.json", "w") as file:
                    # Saving the updated data
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
# ---------------------------- SEARCH CREDENTIALS ------------------------------- #
def search_creds():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"{website} credentials:\nUsername: {username}\n"
                                                       f"Password: {password}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No password data file found")
    except KeyError:
        messagebox.showinfo(title="Error", message=f"No password saved for {website}")
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
website_input = Entry(width=19)
website_input.grid(column=1, row=1)
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

# Search button
search_button = Button(text="Search", width=12, command=search_creds)
search_button.grid(column=2, row=1)

window.mainloop()
