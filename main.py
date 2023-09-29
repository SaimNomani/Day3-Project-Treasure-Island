# You've been provided with a Python code that implements a text-based adventure game called "Treasure Island." This
# game takes the player on a journey where they make choices at different points, leading to either a successful
# treasure hunt or a "Game Over" scenario. Below are the key components of the game:
#
# The player starts at a crossroads and must decide whether to go left or right. Choosing "right" leads to a "Game
# Over" message.
#
# If the player chooses "left," they reach a lake with an island in the middle. Here, they have two options: waiting
# for a boat or swimming across. Opting to swim results in a "Game Over."
#
# If they decide to wait for a boat and successfully reach the island, they encounter a house with three doors: one
# red, one yellow, and one blue. Choosing the blue or red door ends the game, while choosing the yellow door leads to
# the discovery of treasure.
#
# If the player makes an invalid or unexpected choice at any point, they receive a "wrong choice" message.
#
print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

cross_road_choice = (input('''You are at a cross road. Where do you want to go? Type 'left' or 'right' ''')).lower()
if cross_road_choice == "right":
    print("Game Over!!")
elif cross_road_choice == "left":
    lake_choice = (input('''You come to a lake. There is an island in the middle of lake. Type 'wait' to wait for a boat
                         or type 'swim' to swim across.''')).lower()
    if lake_choice == "swim":
        print("Game Over!!")
    elif lake_choice == "wait":
        door_choice = (input('''You arrive at the island unharmed. There is house with 3 doors. One red, one yellow and 
                             and one blue. Which color do you chose?''')).lower()
        if door_choice == "blue":
            print("Game Over!!")
        elif door_choice == "red":
            print("Game Over!!")
        elif door_choice == "yellow":
            print("you got the treasure")
        else:
            print("wrong choice")
    else:
        print("wrong choice")
else:
    print("wrong choice")
