


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


Q.3 what is tokens in python ?
Ans = token is a smallest individual units in python.
There are 5 types :
1. keywords
2. identifiers
3. literals
4. operators
5. punctuators


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
multi line comments"""


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

5. Membership operators 
5.1 in 
5.2 not in 


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
 

<!--                                                                                 STRING IN PYTHON                                                       -->
1. strings in python = string is data type that stores a sequence of character in double and single inverted charcter. strings is immutbale.  
Ex :
1. "himmanshu"
2. "133"


2. operators in stirings = The two basics operators   of strings are + and * have used these operators as arithmetic operators  before for addititon and multiplication respectivley . But  used with strings + operators performs concatenation  rather than addition and operators perfroms replication rather than multiplication . let us see how. 
Example :
"hello"+ "world"= helloworld
"1" +"4" =14 # string concantenation operators rather than addititon
"1" * 5 =11111  # string replication operators rather than multiplication
"2"+ 5= error
"3" * "4" = error


3. comparsion operators in strings =
"a"=="a" will give true
"abc"=="abc" will give true 
"j"=="J" will give false


4. ordinal value of strings = 
characters    ordinal value 
0 to 9        48 to 57 
A to Z        65 to 90
a to z        97 to 122


5.  greator than and lower than in strings =
Ex : 'A' > 'a' # it will give false because A  has 65 and a 97 
'ABC'> 'abc' # it will give false beacause of ordinal value 


6. find ordinal value of and character in python= 
 od() using this we find ordinal value of any character .
Ex :
print(od("a"))
output : 97

6.  find  character by od value= 
Ex:
print(ch(97)) #output is  'a'



7.  len function in string = it means length of a string  see .
Ex :
name="hello"
name2= "world"
name3=name+name2
print(len(name3))  
<!-- output is 10  -->

name4=name+" "+name2
print(len(name4))
<!-- output is 11 -->


8. Indexing in python = Indexing means accessing individual characters of a string using their position (index number).
EXAMPLE:
| Character | P | y | t | h | o | n |
| Index     | 0 | 1 | 2 | 3 | 4 | 5 |


9.  how to access any string by indexing =
EXAMPLE:
text = "Python"
print(text[0])  # P
print(text[2])  # t


10. Negative indexing =
EXAMPLE:
| Character | P  | y  | t  | h  | o  | n  |
| --------- | -- | -- | -- | -- | -- | -- |
| Index     | -6 | -5 | -4 | -3 | -2 | -1 |


11. Slicing in  string  =
Accessing a part of a string . last indexing is not count in both positice as well as negative 
str[ starting _idx : ending :jump  ]
Ex :
str= "apnacollege"
str[1:4] is "pna"
str[ :4] is same as str[0:4]
str[1: ] is same as str[1: len(str)]
str[1:4:2] is same but have jump also p , a ,o 
str[ : :-1] is output is egellocanpa
Ex2:
str="himanshu kumar "
str[-5:] it means "kumar"
str[-5:-1] it means "kuma"


12. string functions= 
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
11. str.title()


13. what is join function in strings =
words ="hello world"

result = " ".join(words)
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
 
2. Statement flow control = they are three types 
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
 
FROM2-

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

4. Range function = The range fun use with pyton loops . The upper and limit also be negative. 
example :
range(1,100,2) # starts from 1 and end to 99 and step not is one is 2.
range(lower_limit, upper_limit , step ) # all value should be integers

example2:
range(1,22,3) # so it means +3 every time output is 1 4 7 10

5. operators in and not in 
let us also take about in operators , which is used with range() in for loops.
to check whether a value is contained inside a list you can use in operators e.g 

EX:
will return false as value 5 is not contained in sequence [1,2,3,4]
  5 in [1,2,3,4]

will return true as value 5 is not contained in sequence[1,2,3,4]
  5 not in [1,2,3,4]

6. The while loops 
A while loop is a conditional loop that will repeat the instruction within itself as long as conditional remains true (boolean true or truth value ). The general from of python while loop is :
  
  while <logicalexpression>:
    loop-body

EX :
a=0 #intailise
while a>0:  #condition
    print("hello",a)
    a=a-3 #increment or decrement 
print("loop is over ")

7. Jump statement - break and continue 
Python offers two jump statement to be used within loops to jump out of loop-iterations . These are break and continue

8. Break statement :
We use in both loops . The break statement enables a program to skip over a part of the code break statement terminates the very loop it lies within execution remains at the statemnt immeadialty

9. Continue statement :
The continue statement skip the value on the particular value 

10. Nested loops :
It means a loops has another loop , first complete inner loop and then complete outer loops
Ex: 
for i in range(1,6):
    for j in range(1,i):
        print("*", end="")
    print()

*
* *
* * *
* * * *


<!--                                                    PYTHON MODULES 

   -->
1. python_modules= A python module is a file which contains some variables constants ,some function . objects , etc defined which can be used in other python programs 

2. python library = A library is collection of module in python.


3. MATH module = you need to  first import to your program for our use in python code 

3.1 math.ceil() # math.ceil(1.13) gives 2.0
3.2 math.sqrt() #give root of the given number
3.3 math.exp()  #give exponential
3.4 math.floor() 
3.5 math.log(num, [base])
3.6 math.pow()
3.7 math.sin()
3.8 math.cos()
3.9 math.tan()
3.10 math.degrees() #radian to degree
3.11 math.radians() #convert degree to radian


4. Random_modules =python random modulees generate random numbers by random modules. 

4.1 random()
4.2 randint()
4.3 randrange(start ,stop ,step)


5. statisctics modules in python= The statistics  module  of python calculate mean , median , mode .

5.1 statistics.mean()
5.2 statistics.median()
5.3 statistics.mode()



<!--                                                      Python basics                                     -->










































