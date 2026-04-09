# # Q.1 Write a program that takes a string with multiple words and then capitalizes the first letter of each word and forms a new strings out of it ?
# # Ans
# string1=str(input("Enter your words: "))
# count=[]
# for i in range(0,len(string1)):
#     if string1[0]== i:
#         string1.capitalize()
#     count.append(string1)
#     num1="".join(count)

# print(num1)

# num1=str(input("Enter a letter: "))
# if num1==num1[ : :-1]:
#     print("It is palindrome")
# else:
#     print("it is not a palindrome ")

# def palindrome():
#     num1=str(input("Enter a letter: "))
#     if num1==num1[ : :-1]:
#         print("It is palindrome")
#     else:
#         print("it is not a palindrome ")
    
# palindrome()
    
s=str(input("Enter your strings :"))
c=str(input("Enter any character :"))
while True :
    if c in s :
        