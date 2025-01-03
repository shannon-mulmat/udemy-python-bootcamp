"""
Topics Covered:
1. If/Else
2. Modulo operator
3. Nested Ifs and Elif
4. Multiple Ifs
5. Logical operators

Project Description:
1. Create a script based on the flowchart: https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D

Completed: 11/19/2024
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You enter a field. Do you want to go 'left' or 'right'? ")

if direction.lower() == "left":
    lake = input("You come to a lake. Do you want to 'wait' for a boat or 'swim'? ")
    if lake.lower() == "wait":
        doors = input("You made it across the lake! You come to a house with 3 doors, 'red', 'yellow', and 'blue'. Which door do you choose? ")
        if doors.lower() == "red":
            print("Burned by fire. Game over.")
        elif doors.lower() == "blue":
            print("Eaten by a bear. Game over.")
        elif doors.lower() == "yellow":
            print("Winner winner chicken dinner!")
        else:
            print("Nope. Game over.")
    else:
        print("Attacked by lake shark. Game over.")
else:
    print("Fall into a hole. Game over.")
