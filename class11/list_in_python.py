#                                                                               SOLVED EXAMPLES
# 7.1Program to print elements of a list[q,w,e,r,t,y] in sepreate lines aloong with elements both indexes ( positive and negative indexes)?
# num1=['q','w','e','r','t','y']
# for i in range(len(num1)):
#     print(f"At indexes {i} and {i-(len(num1))} elements : {num1[i]}")

# 7.2 Extract two list slices out of a given list of numbers . Display and print the sum of elements of first list slices which conatins evary other elements of the list between 5 to 15 
# . Program should also display the average of elements in second list slice that conatins every fouth elements of the list . The given list conatins numbers from 1 to 20.
# L1= [1,2,3,4,5,6,7.8,9,10,11,12,13,14,15,16,17,18,19,20]
# slice1=L1[5:15]
# slice2=L1[::4]
# print(slice2)

# 7.3  Write a program to create a copy of a list . In the list is copy , add 10 to its first and last elements . Then display the lists ?
# L1=[34,65,45,33,66,35,36,68]
# L2=L1
# count=[]
# for i in L1:
#     if L1[0]==i:
#         i+=10
#         count.append(i)
#     elif L1[7]==i:
#         i+=10
#         count.append(i)
#     else:
#         count.append(i)

# print("Original list ",L1)
# print("Copy list ",count)

# 7.4 Write a program that asks the user to input a number  a list to be appended to an exisiting list . Wether the user enters a single number or a list of numbers , the program 
# should append the list accordingly ?



# 7.5  Write a program that display options for inserting or deleting elements in a list . If the user chosses a deletion option , display a submenu and ask if element 
# is to be deleted with value or by using its postion or a list slice is to be deleted ?


# 7.3 Program to find minimum element from a list of element along with its index in the list ?


# 7.4 program to calculate mean of agiven list of members ?
# lst1=eval(input("Enter a list :"))
# length=len(lst1)
# count=0
# for i in range(0,length):
#     count+=lst1[i]

# num2=count/length
# print("Given list :",lst1)
# print("The mean of the given list is :",num2)

# 7.5 Program to search for an element in a given list of numbers ?
# lst1=eval(input("Enter your list: "))
# search=int(input("Enter elements to be searched for : "))
# length=len(lst1)
# for i in range(0,length):
#     if search==lst1[i]:
#         print(search,"found at index",i)
#         break
# else:
#     print(search,"not found in given list ")
# 
# 
# # 7.6  Program to count frequency of a given element in a list of numbers ?
# lst1=eval(input("Enter list: "))
# search=int(input("Enter elements :"))
# count=0
# length=len(lst1)
# for i in range(0,length):
#     if search== lst1[i]:
#         count+=1
# print(f"{search} element frequency is {count}")



# 7.7  Program to find frequencies of all elements of a list . Also print the list of 
# unique elements in the list and duplicate elements in the given list ?
# lst1=eval(input("Enter your list :"))
# count=0
# length=len(lst1)
# for i in range(0,length):
#     if lst1[i]==


#                                           Chat gpt problem of list in python 
# Q.1 Write a program to remove duplicate elements from a list.
# Q.2 Write a program to merge two lists and display the result.
# Q.3 Write a program to create a list of squares using list comprehension.
# Q.4 Write a program to separate even and odd numbers into different lists.

# 1
num1=eval(input("Enter your lists :" ))
length=len(num1)
count=[] #empty list 
for i in range(0,length):
    if num1[i] not in  count :
        count.append(num1[i])

print("New list is ",count)

