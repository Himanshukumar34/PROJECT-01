🧠 What is a Compiler?
A compiler converts your entire code into machine code at once before running it.
🔧 How it works:
You write code
Compiler converts whole program → machine code
Then program runs

✅ Example:
Languages like:
C
C++

⚡ Key points:
Faster execution
Errors shown after full compilation
Output = executable file (.exe)

⚡ What is an Interpreter?
An interpreter runs your code line by line.
🔧 How it works:
Reads 1 line
Executes it
Moves to next line
✅ Example:
Python
JavaScript

Q.2 What is python ?
Ans = 1. python is simple and easy 
2. free and open source
3. high level language 
4. developed by guido van Rossum 
5 . portable


Q.3 what is python character set ?

Ans = 1. letters A to Z ,a to z.
2. Digits - 0 to 9.
3. special symbols -,+,* etc .
4. white spaces - blank spaces , tab , carriage return , new line 
5. other characters - python can process all ascii and Unicode characters .

Q.4 What is variables ?

Ans = A variables means stores a values and store any value .
or means assign the value
example -- name = shraddha 
age = 23 
price = 25.99 etc

Q.5 what is identifiers?

Ans = 1. Identifiers can be combination of uppercase and lowercase letters , digits or an underscore_ .
so myvariable , variable_1 , variable_for_print all are valid python identifiers .
2. An identifiers can not start with digit . so while variable1 is valid , 1variable is not valid .
3. we can not use special symbols like !,#,@,%,$ etc in our idnetifers .
4. Identifier can be of any length .

Q.6 what is data types?

Ans=   1. integers =1,2,3,4 
2. strings="himanshu ", 'himanshu', ''' himanshu '''
3. float = 878.7
4. Boolean = True or False
5. none = means empty value  . Example : num1 =none .


Q.7 what is python keywords ?

Ans = and , else , in , return  as except is True  assert finally lambda try break false nonlocal while with none for class continue from not yield def global or del if pass elif import raise. keywords are reserved words in python means we can not use this word
because already a value reserved in python .
 

Q.8 what is case sensitive in python how to relate them ?

Ans = python is case  sensitive language means capital A or small a are two separate thing while sql is not a case sensitive .
Example :  let a apple variable1 and a Apple variable2  ye dono alag alag variables hai nah ki ek variable hai . 


Q.9 what is python in comments ?

Ans = comments means that which does not execute its is only read purpose .
ex =  # this is comment 
""" this is 
multi line command """


Q.10 what is operators and how many types ?

Ans An operators is a symbols that perform a certain between operands .
ExAMPLES :
a + b = a and b is operands and + is operators.

Types of operators 

1.Arithmetic operators
addition +
subtraction --
multiplication *
divide /
remainders %
a to the power b **

2. Relational operators 
ex :
a= 10 
b=23
print(a==b)# false 
print(a!=b) #true 
print(a>=b)# false 
print(a<=b)# true 



3. Assignment operators 

ex :
1. =	    Assign value
2. +=	        Add and assign = means  x ki vlaue 3 se bada do 
<!-- x = 5
x += 3   # x = x + 3 -->

3. -=	        Subtract and assign = means x ki value 2 se gata do
<!-- x = 5
x -= 2   # x = x - 2 -->

4. *=     	Multiply and assign
<!-- x = 5
x *= 2   # x = x * 2 -->

5. /=	       Divide and assign
<!-- x = 5
x /= 2   # x = x / 2 -->

%=	        Modulus and assign
<!-- same as old -->
**=	    Power and assign
<!-- same as old -->
//=	        Floor divide and assign
<!-- same as old -->

4. logical operator 
4.1 and 
4.2 not 
4.3 or


Q.11 what is conversion in python ? how many types of conversion ?
Ans = conversion means convert data types into another data types like int to string 

🔄 Types of Conversion
1. Implicit Conversion (Automatic)
Python automatically converts one data type to another
Example:
<!-- a = 5      # int
b = 2.5    # float

c = a + b  # int → float automatically
print(c)   # 7.5 -->

2. Explicit Conversion (Type Casting)

User manually converts data type using functions

🔧 Common Conversion Functions
Function	Meaning
int()	Convert to integer
float()	Convert to float
str()	Convert to string
bool()	Convert to boolean


Q.12 what is input in python ?
Ans input () statement is used to accept value (using keyboard) from users .
Result for input() is always string . when you need convert  so convert like int(input()) , float(input())

Q.13 What is escape sequence character in python ?
Ans Escape	Meaning
\n	New line
\t	Tab space
\\	Backslash
\'	Single quote
\"	Double quote
\r	Carriage return
\b	Backspace
\f	Form feed
\v	Vertical tab
 

<!--                                            STRING IN PYTHON                                                         -->
Q.14 what is strings in python?
Ans string is datat type that stores a sequence of character .

Q.15 What is concatenation in string ?
Ans = it means sum of two string is not addiion see.

Example :
"hello"+ "world"= helloworld
"1" +"4" =14


Q.16 What is len function in string ?
Ans it means length of a string  see .
Ex :
name="hello"
name2= "world"
name3=name+name2
print(len(name3))  
<!-- output is 10  -->

name4=name+" "+name2
print(len(name4))
<!-- output is 11 -->

Q.17 what is indexing in python ?
Ans =Indexing means accessing individual characters of a string using their position (index number).
EXAMPLE:
| Character | P | y | t | h | o | n |

| Index     | 0 | 1 | 2 | 3 | 4 | 5 |

Q.18 how to access any string by indexing ?
Ans =
EXAMPLE:
text = "Python"
print(text[0])  # P
print(text[2])  # t

Q.19 what is negative indexing ?
Ans
EXAMPLE:
| Character | P  | y  | t  | h  | o  | n  |
| --------- | -- | -- | -- | -- | -- | -- |
| Index     | -6 | -5 | -4 | -3 | -2 | -1 |


Q.20 What is slicing in  string  ?
Ans Accessing a part of a string . last indexing is not count in both positice as well as negative 
str[ starting _idx : ending :jump  ]

Ex :
str= "apnacollege"
str[1:4] is "pna"
str[ :4] is same as str[0:4]
str[1: ] is same as str[1: len(str)]

Ex2:
str="himanshu kumar "
str[-5:] it means "kumar"
str[-5:-1] it means "kuma"

Q.21 what is string functions ?
Ans =
Example : 
str=" I am a coder"
1. str.endswith("er") # retrun true if string ends with er 
2. str.capitalize() #capitalize only first character 
3. str.replace(old,new)
4. str.find("a") #it returns index of the letter
5. str.count("a") # it gives 2 beacause a is two times i string 
6. str.upper() # it give I AM A CODER
7. str.lower() # it give i am a coder
8. str.isdigit() # it give false because it is not a digit
9. str.isalpha() #it give true beacuse it is aplhabeticall 
10. str.strip()#it remove spaces form starting and end

Q.22 what is join function in strings ?
Ans
words ="hello world"

result = ",".join(words)
print(result)


                                                <!-- conditional statement in python  -->

1. statement= it is line code which is write by him 
ex:
a=13 # statement1
b=a+34 # statement2
c=a+b  # statment3

1.1 Empty statment :
The simplest statment is the empty statement i.e statment which does nothing . In python an empty statement is pass statement
Ex :
a=13
pass

1.2 Simple statemnt :
Any single executable statemnt is a simplest statement in python. 
For example :
name=input("Enter your name")

1.3 Compound statemnt :
A compound statment represents a group of statemnt executed as a unit . The compound statemnt of python are writen in a secific pattern as shown below :
<compund statement header >:
<indented body conatining multiple simple and/or compound statemnts >
this is a compound statement has :
 
2.Statement flow control = they are three types 
1. sequence 
2. selection
3. iteration

2.1 sequence = The sequence construct means the statement are being executed sequentily . This represents the default flow of statement .
Ex :
statement1 then 
statement2 then
statement3 

2.2 selection = The slection construct means the execution of statemnet depending upon a condtion test . If  a condition evaluates true a course of action is followed otherwise another coourse of action is follwoed 

Ex:
condition  ------- true --> statement1 ---> statement2
    false 
     -
     - 
     statement1

2.3 iteration = Its  a type of loops in which contition if true they run againa and again when condition is false the loops is over.

3. if statemnt = An if statement tetsts a particular condition  : if condition ealauates to true  then is executed otherwise not.

4. if -else= 
EX :
if condition :
   statement 
else:
    statement2

5. if elif statement = if you check multiple condititon when we use if elif condition .
ex :
if condition :
    statement1
elif conditon :
    statement2
elif condition :
    statement3
else :
    statement4

6. Nested statement = A nested if is that has another if in its body or in elifs body or in its else is body .

Exmaple :
FROM1 
if condition :
   if condition:
      statement 
   else:
    statement

elif condition :
   statement 
else :
   statements 
 
FROM2

if condition :
    statement 

elif condition :
   if condition :
      statement 
   else:
      statement
   
else :
   statements 



                                                                <!-- LOOPS IN PYTHON -->

1. Repition of tasks a necessity = when you need to repeat same sets of tasks again again 

2. loops = The iteration statements  or repition statements allow a set of instruction to be performed  repedatily untik a certain condition is fulfilled .
The iteration statement are also called loops or looping statements. python provides two kinds of loops : for loops and while loop

  2.1 counting loops :The loops thats repeats a certain number of times python for loop is a counting loops 

  2.2 conditional loops : The loop that repeats until a certain things happens i.e 
  they keeps  repeating as long as some condition is true pythons while loops in conditional loops 

3.For loop =for <variable > in <sequence> :
                  statemnts_to_repeats

4.Range function = The range fun use with pyton loops . The upper and limit also be negative. 
example :
range(1,100,2) # starts from 1 and end to 99 and step not is one is 2.
range(lower_limit, upper_limit , step ) # all value should be integers

example2:
range(1,22,3) # so it means +3 every time output is 1 4 7 10

5. 


























































