"""
Topics Covered:
1. TKinter
2. Widgets
3. *args
4. **kwargs

Project Description:
- Create a GUI that allows the user to enter a number of miles and get back out the equivalent kilometers when they click "Calculate"

Completed: 3/12/2025
"""
from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=km)

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

"""
4 labels:
- "Miles"
- "is equal to"
- result which is "0" until a number is entered in the entry field and the button is clicked to calculate
- "Km"
"""
miles_label = Label(text="Miles")
miles_label.grid(column= 2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

"""
1 button:
- "Calculate"
"""
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

"""
1 entry field:
- Blank on start-up, fill with calculated answer when button is clicked
"""
miles_input = Entry(width=9, )
miles_input.grid(column=1, row=0)

window.mainloop()
