

🐍 Computational Thinking & Programming – Python
1.python fundamentals 
2.Data Handling (Data Types, Variables, Operators)
3.Flow of Control (if, else, loops)
4.Strings
5.Lists
6.Tuples and Dictionaries




<!--                                     PYTHON FUNDAMENTALS                -->
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
5. portable

Q.5 what is global in python?
Ans A global variable is a variable that is:
Defined outside any function
Can be accessed anywhere in the program
Ex: 
x = 10   # global variable

def show():
    print(x)

show()   # Output: 10

Q.3 what is tokens in python ?
Ans = Token is a smallest individual units in python.
There are 5 types :
1. keywords
2. identifiers
3. literals
4. operators
5. punctuators


Q.7 what is python keywords ?

Ans = and , else , in , return  as except is True  assert finally lambda try break false nonlocal while with none for class continue from not yield def global or del if pass elif import raise. keywords are reserved words in python means we can not use this word
because already a value reserved in python .

Q.5 what is identifiers?

Ans = 1. Identifiers can be combination of uppercase and lowercase letters , digits or an underscore_ .
so myvariable , variable_1 , variable_for_print all are valid python identifiers .
2. An identifiers can not start with digit . so while variable1 is valid , 1variable is not valid .
3. we can not use special symbols like !,#,@,%,$ etc in our idnetifers .
4. Identifier can be of any length .

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



Q.6 what is data types?

Ans=   1. integers =1,2,3,4 
2. strings="himanshu ", 'himanshu', ''' himanshu '''
3. float = 878.7
4. Boolean = True(1) or False(0)
5. none = means empty value  . Example : num1 =none .

Q.8 what is case sensitive in python how to relate them ?
Ans = python is case  sensitive language means capital A or small a are two separate thing while sql is not a case sensitive .
Example :  let a apple variable1 and a Apple variable2  ye dono alag alag variables hai nah ki ek variable hai . 


Q.9 what is python in comments ?
Ans = comments means that which does not execute its is only read purpose .
ex =  # this is comment 
""" this is 
multi line comments"""




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
 


<!--                                      Data handling                    -->
1. What is data types ?
Ans= data can be any types e.g integer , real . string etc
Numeric → int, float, complex
Text → str
Sequence → list, tuple, range
Mapping → dict
Boolean → bool
None → NoneType

2. Numbers = As it is clear by the name the number data types are used numeric values in python .

2.1  Intergers = without decimal all the integers
2.2 floating point number = decimal numbers 
2.3 complex number = there are one a real number and one is imaginary number . 2+ 3i   we use z.real() use for accesing the real value and z.img() use for accessing imaginery value


3. strings = A string data types in python hold any value in double quiotes 
Ex : "acbs" , "3435" ,"????" ,"TRUE" etc

4. List = a=["himanshu","true"]

5. Dictionary = { "name" : 34}

6. Tuples = ("hiamsnuh", 65 ,"krishna")


7. Mutable and immutable types = mutable means changeable and immutable means unchangebale .
Immutables types 
1. Integers
2. floating 
3. booleans 
4. strings 
5. tuples 

Mutable types
1. sets 
2. list 
3. dictionary

8. memory = memory of any characters value .
id(5) #65654

9.  Immutable data types = The immutable types are those that can never change their value in place .In python the following types are immutable : integers , floating point numbera , booleans , strings . tuples .
 
Lets us understand the concept of immutable types . In order to understand this , consider the code below  

Sample code 5.1 
p=5 
q=p
r=5
 # will give 5,5,5 sab ke andar 5 hi store hia beacuse every number has memory 

Explain :
id(p)
# 45454545

id(q)
# 45454545

id(r)
# 45454545

so now ulitimatley say that all immutable means the number is store there location the location is not change so it is called immutable data types 
and id use for checking memory of any number .

one more example:
p=10 
r=7
q=r

id(10)
# 676767

id(p)
# 676767

id (7)
# 787878

id(q)
# 787878

10. Mutable data types = The mutable types are those whose values can be changes in place . Only three types are mutable in python . These are list , dicionaries  and sets .

To change a member of a list , you may write :
chk=[2,4,6]
chk[1]=40
It will make the list namely chk as [2,4,6]
Explain :
chk = [2,4,6]
id(chk)
# 54545454

chk[1]=50
id(chk)
# 54545454


📊 Key Differences
Feature	Mutable	Immutable
Changeable	✅ Yes	❌ No
Memory	Same object modified	New object created
Speed	Slightly slower	Faster
Safe	Less safe	More 

11. Varible literals = python is an object oriented language . python calls every entity that stores any values or any types of data as an objects

5.1 The type of an objects = give type of any objects 
5.2 The id of an objects  = gives memory of any elements 
5.3 the values of an objects = gives output of anything


12. Operators = The symbols that trigger the operation / action are called operators and the data on which operation is being carried out i.e the objects of the operations are referreds to as the operands .
Ex : 2+3 # 2,3 are operands and '+' operators

python rich sets of operators comprises of these types of  operators 
12.1 Arithmetic operators 
12.2  Relational operators 
12.3 Identity operators 
12.4 Logical operators 
12.5 Bitwise operators 
12.6 Membership operators 

1. Arithmetic operators=
addition +
subtraction --
multiplication *
divide /
remainders %
a to the power b **
floor division //

They are two types :
1.unary= The unary operators use for  + in one operands .
Ex: num1+=1

2.Binary=operators that acts upon two operands are refferred to as binary operators .
Ex : num1 +num2

* Augmented assignment operators = The assigenment opertors use to assign the operators = which is always use .
EX :
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

2. Relational operators =
ex :
a= 10 
b=23
print(a==b)# false 
print(a!=b) #true 
print(a>=b)# false 
print(a<=b)# true

Relational operators work on the following principles :
. For numeric types the 4 and 4.0 both are equal
. strings a = A are not equal because of unicode number is called lexicographical ordering .

3. Identity operators = These are two identity operators in python is and is not . The identify operators are used to check the operators  are used to check if both the operators refernece te same object memory i.e the identify operators comapare the memory location of two objects and return True ofr False accordingly .

EX:
1. is = a is b  #  return true if both memory location is same .
2. is not = a is not b # return true if both memory loaction is not  same.  

4. logical operator = Pyhton combine three logical operators to combine existing expressions. These are or , and , not .
4.1 The or operators : The or operators two combines two expressions , which make it operands . The or operator works in these ways .
1. Relational expressions as operands 
2. Numbers or strings or lists as operands .

ex :
X          Y       X or Y
False    false     false   #it means when two condtion is false its conditon is false 
false    true      true    # same as the condtion is true and so on.
true     false     true
true     true      true

4.2  The and operators = The and operators two combines two expression , which make them . 
ex: 

false  false  = false 
false  true   = false 
true   false  = false 
true   true   = true 


4.3 the not operators = This is a type of complement of any value .
ex:
a!=b # this is type of not cmeans complenet

5. Bitwise operators =python provde another category of operators of bitwise operators which are similar to the logical operators  excet that they work on a smaller scale on binary represnetations of data . Bitwise operrators a used to change individual bits in an operands. 

python provides following bitwise operators .
Ex : 
And = &
or =|
not = ~
nor =^

* Type casting = python internally changes the data types of some operands so that all operands have same data type . This type of conversion is automatic , timplicit and hence known as implicit type conversion . python however also supports explicit type conversion .

* Explicit type conversion =The type is conversion is users defined that forces an expression to be specfici type . 
Ex :
int()
float()
str()
complex()
bool()

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

5. if elif statement = if you check multiple condititon when we use if elif condition .agar peheli conditon chali toh baki nahi chalehingi aur agar dusiri chali pehli chalne ke baad toh last ki nahi chalngi and so on. 
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

NOTE : agar apne yaha per conditon thi toh toh increment decrement karana padega aur agar true hai toh voh ek infinity loop hai voh toh break statment se hi bahar ayega .

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


<!--                                               List in python                           - - >

1. List = list is a type of sequence like strings and tuples but it differs from them iin the way that list are mutable but strings and tuples are immutable .

Ex: l1=["himanshu ","class",false, 45]

2. Creating and accessing lists = A list is a standard data type of python that can store a sequence of values belonging to any type . the list are depicted through square brackets e.g following are some lists in python .

Ex:
[] #list with no number , empty list 
[1,2,4] # list of integers 
[1,2,5,3.7,9] #list of integers and floating points 
['a','b','c'] # list of characters 
['a', 1, 'b', 3.5 ,'zero'] #list of mixed value type 

A. Creating lists =To create a list , put a number of expressions in square brackets .That is use square brackets to indicate the start and end of the list , and seperate the items by commas . For examples 
[2,4,6]
["adf","reg"]
[]
num1=list() # create a empty list also 
num2=list(34,45,44,"afkd")  #create a long list also 

3.Nested list =A list can have an element in it which itself is a list . Such a list  is called nested list . e.g 
L1 =[3,4,[5,6],7] 
L1 is a nested list with four elements : 3,4 ,[5,6] and 7. L1[2] elements is a 
list [5,6] . length of  L1 is 4 as it counts [5,6] as one elements . Also as L1 [2] is a list which means L1[2][0] will give 5 and L1 [2][1] will give 6. 


7. 
