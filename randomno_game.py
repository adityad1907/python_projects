import random 

num = random.randint(1,100)

a = int(input("Enter a number: "))

while a != num:
    if a < num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    a = int(input("Enter a number: "))
    if num == a:
        print("Congratulations! You guessed the number!")
    else:
        print("Sorry, try again!")
        

