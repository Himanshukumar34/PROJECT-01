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

#                       SOLVED EXAMPLES 
# Q.1  write a program that takes a string with multiple and then capitalize the first 
# letter of each word and forms a new string out of it ?

# string2=input("Enter your line :")
# new_string=[]
# for i in string2:
#     if i==string2[0]:
#         new_string.append(i.capitalize())
#         num2="".join(new_string)
#     else:
#         new_string.append(i)

# print("your old string :",string2)
# print("your new string :",num2)

