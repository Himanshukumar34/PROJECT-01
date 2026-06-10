# Chatgpt task 
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


# Q.9 Print fibonacci series up to n terms ?
num1=int(input("Enter where you want to make fibonacci series :"))
if 















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
# count=1
# fact=0
# for i in range(1,num1+1):
#      num1=count*i
# print(num1)


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











