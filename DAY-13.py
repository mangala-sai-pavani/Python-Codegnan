'''
Function: 
--> It is a block of code that can be reusable.
--> A function can only run when it is called.
--> def is the keyword used to define the function.
--> function is defined only once while it can be called multiple times.
syntax:
def func_name(parameters):
     code
func_name(arguments)

o Required Arguments: Function must call with the correct number of arguments, that means if function expects two arguments
we have to call the function with two arguments not less or not more.
ex: def even_odd(num,num_2):
       print(num+num_2)
    even_odd(9,8)
    even_odd(9,8,90)#type error bcz difference in no. of parameters.

o Default Arguments: By default ,value is taken from the parameter if there are no arguments given.
ex:
def display(name = "ris"):
    print(f"hello,{name}")
display("Ritu") #hello,Ritu
display("Ritika") #hello,Ritika
display()#hello,ris

o Keyword Arguments: Here, we can send arguments with key = value syntax. By this, the order of arguments does not matter.
ex:
def add(num_2,num_3,num):
    print(num+num_2+num_3)
add(num = 9,num_2 = 8,num_3 = 1)
#Output: 18

o Variable Length Arguments: Add a star(*) before the parameter namee in the function,receive a tuple of arguments and can access
items with indexes.
ex:
def display_2(*name): # used when we do not know how many arguments have been passed
    print(name[1])
display_2("priyanshi","shweta","mrudula")

'''
num = int(input())
def even_odd(num):
    if num%2 ==0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
even_odd(num)
even_odd(63) # an example for reusability.
#Output-1: 6 is an even number.
#Output-2: 63 is an odd number.

def display(name = "ris"):
    print(f"hello,{name}")
display("Ritu") #hello,Ritu
display("Ritika") #hello,Ritika
display()#hello,ris

def add(num_2,num_3,num):
    print(num+num_2+num_3)
add(num = 9,num_2 = 8,num_3 = 1)
#Output: 18

def display_2(*name): # used when we do not know how many arguments have been passed
    print(name[1])
display_2("priyanshi","shweta","mrudula")
