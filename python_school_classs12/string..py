#                            Chatgpt task
# Q.1 Take a string input and print it in reverse 

# Approach01
# num1=str(input("Enter your string :"))
# count=[]
# for i in num1:
#     count.append(i)
#     count.reverse()
#     num3=" ".join(count)

# print(num3)

# Approach02
# string=str(input("Enter your string :"))
# print(string[ : :-1])

# Q.3 Find the frequency of each character from a string ?
num1=str(input("Enter you string in input  :"))






























#                                      Chatper =9   string pratice problem

# Q.9.1 program to read a string and display it in reverse order display one charcter per line do not create a reverse string , just display in revrse 
# order?
# strings1= input("Enter your strings : ")
# length=len(strings1)
# for i in range(-1,-length,-1):
#       print(strings1[i])


# Q.9.2 program to read a string and display in it the from ?
# string1=str(input("Enter your name :"))
# for i in string1:
#       print(i)
# length=len(string1)
# for j in range(-1, -length-1,-1):
#       print(string1[j])

# Q.9.3 program that reads a line and a substring . It should then display the number
# the occurence of the given substring in the line ?
# line=str(input("Enter line :"))
# sub=str(input("Enter substrings  :"))
# count=[]
# for i in line :
#     if i ==

# Q.9.4 program that prints the following pattern without using any nested loop?
#
# #
# # #
# # # #
# # # # # 
# for i in range(1,5):
#     print("#"*i)

# Q9.5 program that reads a line and prints its statics like 
# count uppercase and lowercase and alphabets and digits in the program ?
# line=input("Enter a line  : ")
# uppercase =lowercase=0
# digitcount= alphabets=0
# for i in line:
#     if i.isupper():
#         uppercase+=1
#     if i.islower():
#         lowercase+=1
#     if i.isalpha():
#         alphabets+=1
#     if i.isdigit():
#         digitcount+=1
# print("Number os uppercase letters :",uppercase)
# print("NUmber of lowercase letter ",lowercase)
# print("Number of alphabets :",alphabets)
# print("Number of digits :",digitcount)


# Ncert Question 
# Q.1 Write a program to input lines of text from the user until enter is pressed .
# Count the total number of character in the text (inculding white spaces) ,total number of alphabets , total number os digits 
# ,total number of special symbols and total number os words in the given text . 
# (Assume that each word is seperated by one space)?
num1: str=input("Enter your text :")
alphabets=0
digit=0
symbols=0
words=0
for i in num1:
    if i.digit():
        digit+=1
    elif i.alpha():
        alphabets+=1
    elif i.


print(f"Total number of character :{len(num1)}")