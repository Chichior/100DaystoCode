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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of a lake. Type "wait" to wait for a boat. Type "swim to swim across.').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?").lower()
    if choice3 == "red":
      print("It is a room full of red hot fire. Much like the color of the door. Really makes you think right? Game Over.")
    elif choice3 == "yellow":
      print("Yellow is gross. Game Over.")
    elif choice3 == "blue":
      print("You Win! Because blue is a SUPERIOR COLOR.")
    else:
      print("You had three options. THREE. WAS THIS ONE OF THE OPTIONS?? NO!!! GO BACK TO KINDERGARTEN. Game Over.")
  else:
    print("Why. Why would you swim in some random lake. Full of random liquid. It was a literal acid pool. Game Over.")
else:
  print("You fell off a cliff. Idiot. Watch where you\'re going. Game Over.")