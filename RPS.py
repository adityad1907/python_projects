print("-----------Rock Paper Scissor-----------")
import random as rand

options = {"1": "Rock",
           "2": "Paper",
           "3": "Scissor"}
#           key   values
#here we use list which convert dict in list so as options we use keys not values so to get no. 
for key , value in options.items():
    print(f"{key:2} {value}")
while True:
    player = int(input("Enter the serial number from the option to play: "))
    robot = rand.randint(1,3)
    win = robot - player 
    print(f"Player Chose:{options[player]}")
    print(f"Robot Chose:{options[robot]}")
    
    if win == 0:
       print("it's a tie")
    elif win > 0 and win % 2 != 0:
       print("The bot wins")
    else:
       print("You win")
else:
    print("Enter the vaild option.")


        
    
         



    











