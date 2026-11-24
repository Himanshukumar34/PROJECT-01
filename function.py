def vowels(num2):
    num1="a,e,i,o,u"
    count=0
    for i in num2:
        if i in num1:
            count+=1
    print("your total vowels = ",count)
            
    
vowels("himanshhu")
