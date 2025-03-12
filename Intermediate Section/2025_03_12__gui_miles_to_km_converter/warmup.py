def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6, 2, 1, 4))

def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
        print(kwargs["add"])

    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        self.color = kwargs.get("color") # .get() will return None if an arg is not provided by the user
        self.seats = kwargs["seats"]

my_car = Car(make="Nissan", model="GT-R", seats="4")
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)


"""
Warmup for the lesson on Tkinter
"""
from tkinter import *

def button_clicked():
    new_text = input.get()
    label.config(text=new_text)

window = Tk()
window.title("My GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
label = Label(text="I'm a Label", font=("Arial", 24, "bold"))
label.config(text="New Text")
label.config(padx=50, pady=50)
# label.pack() # default placement = top center
# label.place(x=100, y=200) # can specify exact x and y coordinates
label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New Button
button = Button(text="New Button", command=button_clicked)
button.grid(column=2, row=0)

# Entry aka input
input = Entry(width=10)
input.grid(column=3, row=2)

"""
From Tkinter Widgets course file
"""
#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
