import random 
num2="rock","paper","scissor"
while True:
    num1=random.choice(num2)
    num3=str(input("Enter (rock,paper,scissor): "))
    if num3==num1:
       print("Game is tie")

    elif num3=="rock" and num1=="paper":
        print("you lose the game try again ")

    elif num3=="scissor" and num1=="rock":
        print("you lose the game try again ")

    elif num3=="paper" and num1=="scissor":
        print("you lose the game try again ")

    elif num3=="paper" and num1=="rock":
        print("you win the game ")
        break

    elif num3=="rock" and num1=="scissor":
        print("you win the game ") 
        break
     
    elif num3=="scissor" and num1=="paper":
        print("you win the game ") 
        break