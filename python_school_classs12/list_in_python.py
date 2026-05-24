
# # Example
# L1=list("hello")
# print(L1)


# l2=[3,5,5,6,[34,45],9]
# print(l2[4][0])

# L=[34,55,46,35,36]
# 34 in L
# # output is False
# 35 not in L
# # output is false

# SOLVED EXAMPLES
# Q.1 Program to print elements of a list[q,w,e,r,t,y] in sepreate lines aloong with elements both indexes ( positive and negative indexes)?
# num1=['q','w','e','r','t','y']
# for i in range(len(num1)):
#     print(f"At indexes {i} and {i-(len(num1))} elements : {num1[i]}")

# Q.2 Extract two list slices out of a given list of numbers . Display and print the sum of elements of first list slices which conatins evary other elements of the list between 5 to 15 
# . Program should also display the average of elements in second list slice that conatins every fouth elements of the list . The given list conatins numbers from 1 to 20.
# L1= [1,2,3,4,5,6,7.8,9,10,11,12,13,14,15,16,17,18,19,20]
# slice1=L1[5:15]
# slice2=L1[::4]
# print(slice2)

# Q.3 Write a program to create a copy of a list . In the list is copy , add 10 to its first and last elements . Then display the lists ?
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

# Q.4 Write a program that asks the user to input a number  a list to be appended to an exisiting list . Wether the user enters a single number or a list of numbers , the program 
# should append the list accordingly ?

# Q.5 Program to find minimum element from a list of elements along with its index in 
# the list?

# Q.6 program to calculate mean of agiven list of members ?
# lst1=eval(input("Enter a list :"))
# length=len(lst1)
# count=0
# for i in range(0,length):
#     count+=lst1[i]

# num2=count/length
# print("Given list :",lst1)
# print("The mean of the given list is :",num2)

# Q.6 Program to search for an element in a given list of numbers ?
lst1=eval(input("Enter your list: "))
search=int(input("Enter elements to be searched for : "))
length=len(lst1)
for i in range(0,length):
    if search==lst1[i]:
        print(search,"found at index",i)
        break
else:
    print(search,"not found in given list ")