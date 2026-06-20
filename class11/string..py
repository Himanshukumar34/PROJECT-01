#                            Chatgpt task
# Q.1 Replace all vowels with * ?
# num1=str(input("Enter your string :"))
# vowels="a,e,i,o,u"
# vowels2="a,e,i,o,u".upper()
# count=[]
# for i in num1:
#     if i not in vowels:
#         count+=i
#     if i in vowels or i in vowels2:
#         count+="*"
# num2=" ".join(count)
# print(num2)

# Q.2 Remove all spaces from a string ?
# num1=str(input("Enter your line :"))
# for i in num1:
#     if i.isalpha():
#         print(i,end="")

# Q.3 Count number of words in a string ?
string1=str(input("Enter your characters of line :"))

        
# Q.4 Print characters at even index?
# num1=str(input("Enter your character :"))
# length=len(num1)
# for i in range(0,length+1):
#     even=i%2
#     if even==0:
#         print(num1[i])

# Q.5 Find common characters from two strings ?
# Approach01
# string1=str(input("Enter you character1 :"))
# string2=str(input("Enter your character2 :"))
# count1=[]  #list
# for i in string1:
#     if i in string2:
#         count1.append(i)
# Common="".join(count1)
# print("Common character in two strings",Common)

    









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

# alphabets=0
# digit=0
# symbols=0
# words=0
# while True:
#     num1: str=input("Enter your text :")
#     if num1.alpha():
#         alphabets+=1
    

# print(f"Total number of character :{len(num1)}")

                                                    #    Ncert exercie
# Q.1                                                    