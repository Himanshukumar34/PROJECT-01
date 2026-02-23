# kriana store in calculator using python
sum=0
while True:
    num=input("Enter thr price item or enter q for exit :")
    sum+=num
    if num=="q":
       print("Thanks you ")
       break
    else:
        print(f"Order total so far :{sum}")
        