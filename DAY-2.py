'''
*Variables - To store data types

o To define a variable we have 2 Rules:
     1. Good ways to define a variable(no error)
         - can start with A-Z,a-z and _
         -can contain 0-9
     2. Bad ways to define a variable(will generate an error)
         -shouldnt start with numbers/digits
         -shouldnt contain any special charecters including space
         -cant contain keywords
--> variable names must be specific or meaningful , so it would be
    easy to get an idea of what the data is abt / who it is abt.

o NOTE:
   o we are going to use meaningful words or name for defining variables.

*Keywords - They are certain words that have already been defined.
   - These keywords can not be used by a variable.
   - Also known as identifiers and reserved words.
   ex: print,if,else,for,range...
*Token - It is the small python code/program to perform a task.
  ex: a,b,c = 10,20,30
      print(f"Difference of a,b,c = {a-b-c}")
*Comments : It is used to explain the code.
            - They wont be considered by the cursor n hence wont be executed.
  o 2 Types:
    - Single line Comment : It is used to explain about that particular line in the code.
      - used to comment only for a line.
      - #,'',"" are used in single line comment.
    - Multi line Comment :  It is used to comment more than a single line / in multiple lines.
      - ''' ''',""" """ are used in multi line comment.
*Boolean type: This is used to find out whether the statement is true or false.
    
'''
X=789
print(X)
x=8765
print(x)
_g=678
print(_g)
num_1=887
print(num_1)
#9o=90    --> will generate an error
#$num=90  --> will generate an error
#ab op=76 --> will generate an error
#ab$y=12  --> will generate an error

# Multiple Variable-Value Assignment
a,b,c = 10,20,30
print(f"a={a}")
print(f"b={b}")
print(f"c={c}")
print(f"Sum of a,b,c = {a+b+c}")
print(f"\n{a} \n{b} \n{c}")

#To check if 2 variables are equal
n1=789
n2=987
print(f"n1==n2 : {n1==n2}")

# To check if the given number is even or odd
num=7
if num%2==0:
    print(f"\n{num} is Even Number.")
else:
    print(f"\n{num} is Odd Number.")


