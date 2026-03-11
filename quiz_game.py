while True:
    user=str(input("you want to play quiz game :"))
    if user=="yes":
        count=0
        while True:
            num1=input("Q.1 python is compiler or interpreter ?").upper()
            if num1=="compiler".upper():
                print("correct answer ")
                count+=10 
            else:
                print("wrong answer ")

            num2=input("Q.2 what is list are mutable or not ?").upper()
            if num2=="mutable".upper():
                print("correct answer")
                count+=10
            else:
                print("wrong answer ")

            num3=input("Q.3 WHAT is the output print(hello) ? :").upper()
            if num3=="error".upper():
                print("correct answer")
                count+=10
            else:
                print("wrong answer ")

            print(f"your total score is {count} points ")
            break
    else:
        print("Thanks you ")
        break



