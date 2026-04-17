# #                                                           FLOW OF CONTROLS

#                                                               EXAMPLES
# Q.1 program that inputs three numbers and calculates two suma as per this .
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


# Q.2 program to find the multiples of a numbers the divisor out of the given five numbers?
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

# Q.3 program to prints the sum of natural numbers betweemn 1 to 7 . print the sum progressively i.e after adding each natural number , print sum so far ?
# count=0
# for j  in range(1,8):
#     count+=j
#     print("sum of natural number 0 to 7 ",count)


# Q.4 program to calculate the foactorial of a number ?
# num1=int(input("Enter your num1: "))
# count=0
# for i in range(1,num1+1):
#     num1*num1

# Q.5 program to calculate and print the sums of even  and  odd intergers of the first n natural numbers ?
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

# Q.7 program to input a number and test if its a prime number ?
# num1=int(input("Enter your number :"))
# num2=num1%1 
# num3=num1%num1
# if num2==0 and num3 == 0:
#     print("IT is a prime number ")
# else:
#     print("It is not a prime number ")




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

for i in range(0,7,2):
    for j in range(0,i):
      print(j, end="\n")
    
















# #                                                                          NCERT GUIDLINES 
# # Q.1 write a program that prints minimum and maximum of five numbers eneterd by the user?
# a=int(input("Enter your num1 :"))
# b=int(input("Enter your num1 :"))
# c=int(input("Enter your num1 :")) 
# d=int(input("Enter your num1 :")) 
# e=int(input("Enter your num1 :")) 
# max, min= 
# Q.2 Write a progam to check if the year entered by the user is a leap ?

# Q.3 write a program to find the sum of digit of an integers number , input by the user? 
# num1=int(input("Enter your numbers :"))

# # Q.4 write a program to print that ?
# for i in range()

