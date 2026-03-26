print("------NUMBER GUESSING GAME------")
print("Rules you have 8 turn to finish the game")
print("you chosse number between 1 and 100")
def num1():
    import random 
    num1=random.randint(1,100)
    count=8
    while count>=0:
        choice=int(input("Enter your guess :"))
        if choice == num1:
            print("congrats you win ")
            break
        elif choice> num1:
            print("your guess is to big ")
        elif choice< num1 :
            print("your guess is to small")
        else :
            print("you lose ")
        count-=1
        print("you have now turn left",count)

while True:
    choice=str(input("you want to play again (y/n) :"))
    if choice=="y":
        num1()
    else:
        print("Thanks you ! good bye ")
        break