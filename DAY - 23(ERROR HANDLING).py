"""
Error Handling:
--------------
o try:
-->The try block ,will test a block of code for errors.
ex:
try:
    print(num)
except:  #this will handle all kind of errors
    print("It is handling NameError/Error")
print("Ris")

o except:
-->This block will handle the error,which are written in the try block.
ex:
try:
    print("python"+9) # since its causing an error it wont proceed with next statements
    print(num)
except NameError: #this will only consider NameErrors
    print("It is handling NameError")
except TypeError:
    print("Handling TypeError")
o Types of Error:
ValueError 
ZeroDivisionError 
IndexError 
TypeError 
FileNotFoundError 
NameError

o else:
--> the else keyword to define a block of code to be executed if no error is raised.
ex:
try:
    print("hi")
except :
    print("It is handling Error")
else:
    print("No error")

o finally:
-->The finally block will execute whether there's an error with try block or not.
ex:
try:
    print(num)
except NameError:
    print("It is handling NameError")
else:
    print("It has no error")
finally:
    print("It is always executed")

#User defined Exceptions

class MyError(Exception):
    pass
age = int(input())
try:
    if age < 18:
        raise MyError("Age must be 18 or above")
    else:
        print("Eligible to vote")
except MyError:
    print("Logical Error")
except error as e:
    print(e)
"""