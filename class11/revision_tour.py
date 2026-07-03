# Write a program that inputs an integer in range 0-999 and then prints if the integer entered is a 1/2/3 digit number ?
# num1 = int(input("Enter a number between 0-999 :"))
# if num1<10:
#     print("It is a single digit number : ")
# elif num1<100:
#     print("It is a two digit number : ")
# elif num1<1000:
#     print("It is a three digit number : ")

# Appraoch02
# num1=int(input("Enter a number between 0-999: "))
# if num1<0 or num1>999:
#     print("Inavlid entry ")
# else :
#     if num1<10:
#        print("It is single digit number  ")
#     else: 
#         if num1<100:
#             print("It is a two digit number ")
#         else:
#             if num1<1000:
#                   print("It is a three digit number ")
    
# Q1.5 Write a program to print cube of numbers from 15 to 20 ?
# for i in range(15,21):
#     print(f"Cube of {i} is {i*i*i}")

# Q1.8 Write a program that multipes  two integer numbers without using the * operator
# using the repeated  addition? 
# n1=int(input("Enter you num1 :"))
# n2=int(input("Enter your num2: "))
# product=0
# for i in range(1,n2+1):
#     product+=n1

# print("Your product is ", product)

#Q1.7 Write a program to print square root of every alternate number in the range 1 to 10?

# Q1.8 Program that reads a line and prnts its statistics like :
# Number of uppercase letters:
# Number of lowercase letters :
# Number of alphabets :
# Number of digits :

line=input("Enter a line :")
lowercount=uppercount=0
alphabets=digits=0
for i in line:
    if i 