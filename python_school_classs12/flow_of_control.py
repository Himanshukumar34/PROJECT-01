#                     Chatgpt task 
# Q.1 check whether a number is positive , negative or zero?
# num1=int(input("Enter your number to check it it positive , negative or zero :"))
# if num1>0:
#      print("It is postive number ")
# elif num1<0:
#      print("It is negative number")
# else:
#      print("It is zero")

# Q.2 Take marks as input and print grade ?
# num1=int(input("Enter your marks for calcluating grade :"))
# if num1>=90:
#     print("Grade A")
# elif num1<89 and num1>75:
#     print("Grade B")
# elif num1>50 and num1<74:
#     print("Grade c")
# else:
#     print("Fail")

# Q.3 Find the largest of 3 numbers ?
# num1=int(input("Enter your number 1 :"))
# num2=int(input("Enter your number 2 :"))
# num3=int(input("Enter your number 3 :"))
# if num1>num2 and num1>num3:
#     print("The largest number is ",num1)
# elif num2>num1 and num2>num3:
#     print("The largest number is ",num2)
# else:
#     print("The largest number is ",num3)

# Q.4 Check whether is year is a leap year or not?
# homework

# Q.5 Print the sum of first n natural number  ?
# n=int(input("Enter your n natural number :"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)
    
# # Q.5 count how many numbers between 1-100 are divisble by 3?
# num1=6
# count=0
# for i in range(1,num1+1):
#     if num1%3==0:
#         count+=1
# print(count)

# Q.7 Input a character and check whether it is a vowels or constonant ?
# num1=str(input("Enter character to check it is vowelsa or constonant :"))
# vowels=["a","e","i","o","u"]
# v1=0
# c1=0
# for i in num1:
#     if i in vowels:
#         v1+=1
#     else:
#        c1+=1
# print("total number of vowels",v1)
# print("total number of consonant",c1)

# Q.8 check whether a number is a palindrome ?
# p1=str(input("Check the name is palindrome or not :")) #approach01
# if p1==p1[ : :-1]:
#     print("It is an palindrome ")
# else:
#     print("It is not an palindrome ")

#approach02
# p1=str(input("Check the name is palindrome or not :"))
# l1=[]
# l1.append(p1)
# l1.reverse()
# print(l1)
# num1="".join(l1)
# if p1==num1:
#     print("It is a palindrome ")







# #                                                           FLOW OF CONTROLS
#                                                                  EXAMPLES
#                 
#Q=4.1 Program to accept three integers and print the largest of the three . Make use only if statement ?


# 4.3 program that inputs three numbers and calculates two suma as per this .
# sum1 as the sum of all input numbers 
# sum2 as the sum of non duplicate  numbers if there are duplicatees numbers in the input ignores them ?
# a=int(input("Enter your num1 :"))
# b=int(input("Enter your num1 :"))
# c=int(input("Enter your num1 :"))
# sum1=a+b+c
# print("sum of the given three number are ",a+b+c)
# sum2=0
# if a!=b and a!=c:
#     sum2+=a
# if  b!=c and b!=a:
#     sum2+=b
# if c!=a and c!=b:
#     sum2+=c
# print("sum of non duplicate numbers is ", sum2)


# 4.5  program to find the multiples of a numbers the divisor out of the given five numbers?
# a=int(input("Enter your num1 :"))
# b=int(input("Enter your num1 :"))
# c=int(input("Enter your num1 :"))
# d=int(input("Enter your num1 :"))
# e=int(input("Enter your num1 :"))
# divisor =input("Enter your num1 :")
# if a%divisor == 0:
#     print(f",Multiple of {divisor } is {a}")
# if b%divisor == 0:
#     print(f",Multiple of {divisor } is {b}")
# if c%divisor == 0:
#     print(f",Multiple of {divisor } is {c}")
# if d%divisor == 0:
#     print(f",Multiple of {divisor } is {d}")
# if e%divisor == 0:
#     print(f",Multiple of {divisor } is {e}")


# 4.6 Program to display a menu for calculating area of a circle or perimeter of a circle?
# while True:
#     radius=bool(input("Enter your radius of circle :"))
#     print("1.Calculate area")
#     print("2.Calculate perimeter")
#     choice = int(input("Enter your choice :"))
#     if choice==1:
#         print(3.14159*radius*radius)
#     elif choice==2:
#         print(2*3.14*radius)

# Q 4.9 Program to print whether a given character is an uppercase or a lowercase character or a digit or any other charcter ?
# num1=input("Enter a single character :")
# if num1.isdigit():
#     print("It is a digit")
# elif num1.upper():
#     print("It is an uppercase letter ")
# elif num1.lower():
#     print("It is an lowercase letters ")
# else:
#     print("It is a special character")

# Q4.10 Program to calculate and print roots of a quadratic equation : ax^2+bx+c=0
# Apporach01  Pending 
# import math
# print("For equation ax^2+bx+c enter there a , b and c :")
# a=int(input("Enter you value of a :"))
# b=int(input("Enter you value of b :"))
# c=int(input("Enter you value of c :"))
# discrimnant=(b*b)-(4*a*c)
# Roots=-b*b+

# Q4.11 Program to print the table of a number ?
# Apporach01
# n=int(input("Enter your number :"))
# for i in range(n,n*11,n):
#     print(i)

# #Apporach02
# n=int(input("Enter your number :"))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")

# Apprach03
# n=int(input("Enter your number :"))
# k=1
# while k<=10:
#      num1=n*k
#      print(f"{n} * {k} ={num1}")
#      k+=1

# Q4.13 program to prints the sum of natural numbers betweemn 1 to 7 . print the sum progressively i.e after adding each natural number , print sum so far ?
# count=0
# for j  in range(1,8):
#     count+=j
#     print("sum of natural number 0 to 7 ",count)


# Q4.14 program to calculate the foactorial of a number ?
# num1=int(input("Enter your num1: "))
# count=1
# for i in range(0,num1):
#     count*=num1-i
# print("Factorial of the number is :",count)


# Q4.15 program to calculate and print the sums of even  and  odd intergers of the first n natural numbers ?
# num1 = int(input("Enter your natural number : "))
# even=0
# odd=0
# for i in range(0,num1+1):
#     num2=i%2
#     if num2== 0 :
#         even+=num2
#     elif num2!=0:
#         odd+=num2
# print("The sum of even integers is ", even)
# print("The sum of odd integers is " , odd )

# Q.6 program to input some numbers repeaditly and print their sum . till the use not say  no to enter more numbers ?
# count=0
# while True:
#     user=str(input("want to enter more numbers :"))
#     if user=="yes":
#           num1=int(input("Enter number :"))
#           count+=num1
#     elif user=="no":
#         print("your total sum is ",count)
#         break

# Q4.19 program to input a number and test if its a prime number ?
# num1=int(input("Enter your number :"))
# num2=num1%1 
# num3=num1%num1
# if num2==0 and num3 == 0:
#     print("IT is a prime number ")
# else:
#     print("It is not a prime number ")

# Program that reads three numbers (integers ) and prints them in ascending order?





#                                                      SOLVED PROBLEMS 
# # Q.1 calculate factorials ?
# num1=int(input("Enter your number :"))
# count=1
# count2=0
# for i in range(1,num1):
#     i+=1
#     count*=i
#     count2+=count
# print(count)


# # Q.2 write a program to input a 6 digit number and divide it into three 2 digit numbers ?
# num1=int(input("Enter your numbers  "))
# if num1>=100000:


# Q.3 Write a program to input two integers x and n comput x ki power n using a loop ?

# x=int(input("Enter your value of x :"))
# n=int(input("Enter your value of n :"))
# count=1
# for i in range(1,n+1):
#     count*=x
# print(count)


# Q.4 numbers in mersenne in the from 2 ki power n - 1 , 2 ki power 2 - 1?


# Q.5 wirte a python sript to print the following patterns ?
# 1
# 1 3
# 1 3 5 
# 1 3 5 7

# for i in range(0,7,2):
#     for j in range(0,i):
#       print(j, end="\n")
    

# # Q.6 write a program to find the sum of the series ?

# num1=int(input("Enter the value of x :"))
# n =int (input("Enter valle of n: "))
# sum=0
# for i in range(0,n+1):
#      sum+=num1**i

# print(sum)

# Q,11 write a program to input the value of x and n and  print the sum of the series ?
# x=int(input("Enter your x  :"))
# n=int(input("Enter your x  :"))

# `# Q.12  write a progam to find the sum of digit of an integers numbers , input by the user ?
# num1=input("Enter the value :")
# count=[]
# for i in num1:
#     count.append(i)
# num=0
# for i in count:
#     num+=i
# print( num1)`

#                                            NCERT GUIDLINES 
# Q.3 Write a program that prints minimum and maximum of five numbers entered by the user ?
# program to input five numbers and print the largest and smallest numbers.
# num1=int(input("Enter your five numbers : "))
# num2=int(input("Enter your five numbers : "))
# num3=int(input("Enter your five numbers : "))
# num4=int(input("Enter your five numbers : "))
# num5=int(input("Enter your five numbers : "))

# Approach01
maximum=0
minimum=0
while True:
    num1=int(input("Enter your number :"))
    

# Q.5 Write a program to generate the sequence -5,10,-15,20,-25...... upto n is an integer input
# by the user ?
while True:
    n=int(input("Enter your n :"))
    







    

# Q.6 Write a program to find the sum of 1+1/8 +1/27........ 1/n ki power 3
# where n is the number input by the user ?



