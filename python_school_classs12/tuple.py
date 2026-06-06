#  Solved examples 
# Q.1 program to print elements  of a tuple ("hello",isn't,"python","fan") in seperate lines along 
# with element's both indexes (positive and negative)?
t= ("hello","isn t","python","fan","?")
length=len(t)
for i in range(0,length):
    print(f"At indexes {i} and {i-length} element :{t[i]}")

# Q.2 Given a tuple namely cars storing car names as elements ?
# ("toyota",'honda','gm','ford','BMW','volswagin','mercedes','ferrai','porsche')
# Write a program to print names of the cars in the index range 2 to 6 both inclusive 
# The output should also inculde the index in words as shwon below ?

t1=("toyota",'honda','gm','ford','BMW','volswagin','mercedes','ferrai','porsche')
for i in range(2,7):
    print(f"index at{i} = {t`1[i]}")
