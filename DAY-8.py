'''
o User Input:
ex:
--> #int datatype input
val = int(input("Enter a Number: "))#Enter a Number: 23
print(type(val))
#Output: <class 'int'>
--> #str datatype input
val_1 = input("Enter a String: ") # Enter a String: abcd
print(type(val_1))
#Output: <class 'str'>
--> #List datatype input
list_1 = list(map(int,input("Enter numbers into the list: ").split())) #Enter numbers into the list: 1 2 34 455 66
print(list_1)
#Output: [1, 2, 34, 455, 66]
print(type(list_1))
#Output: <class 'list'>
--> #Tuple datatype input
t_1 = tuple(map(int,input("Enter numbers into the tuple: ").split())) #Enter numbers into the tuple: 1 22 33 44 55
print(t_1)
#Output: (1, 22, 33, 44, 55)
print(type(t_1))
#Output: <class 'tuple'>
--> f- string or doc string:
a=98
b=66
print("A+B = ",a+b)
#Output: A+B = 164
print(f"A+B = {a+b}")
#Output: A+B = 164
print(f"{a}+{b} = {a+b}")
#Output:98+66 = 164

---> eval(): it considers the the datatype of the value entered by the user if the input is in list type would be list n it would
             conider that datatype.
             ex: #EVAL FUNCTION -- eval()
             val = eval(input("Enter the value: ")) #Enter the value: (1,2,3)
             print(type(val))
             #Output: <class 'tuple'>
             print(val)
             #Output: (1, 2, 3)

STATEMENTS:
----------
    -> Conditions :
          - if
          - elif
          - else (fallback statement)
          - nested if
    -> Control :
          - break
          - continue
          - pass
    -> Loop :
         - for
         - while

 o if statement: it is used to check if a given condition is true or not.
-> program:
val=9
if val >= 9:
    print(f"{val} is greater than or equal to than 9 ")
    
 o else statement: it is a fallback statement,incase if statement becomes false,it will enter into else block.
-> program
val=9
if val > 9:
    print(f"{val} is greater than 9 ")
else:
    print(f"{val} is not greater than 9 ")
#Output: 9 is not greater than 9


'''

#int input
val = int(input("Enter a Number: "))#Enter a Number: 23
print(type(val))
#Output: <class 'int'>
#str input
val_1 = input("Enter a String: ") # Enter a String: abcd
print(type(val_1))
#Output: <class 'str'>

#passing two variables
a,b = map(int,input("Enter 2 numbers: ").split()) #Enter 2 numbers: 34 56 
print(a)
#Output: 34
print(type(a))
#Output: <class 'int'>
print(b)
#Output: 56
print(type(b))
#Output: <class 'int'>

#List datatype
list_1 = list(map(int,input("Enter numbers into the list: ").split())) #Enter numbers into the list: 1 2 34 455 66
print(list_1)
#Output: [1, 2, 34, 455, 66]
print(type(list_1))
#Output: <class 'list'>

#Tuple datatype
t_1 = tuple(map(int,input("Enter numbers into the tuple: ").split())) #Enter numbers into the tuple: 1 22 33 44 55
print(t_1)
#Output: (1, 22, 33, 44, 55)
print(type(t_1))
#Output: <class 'tuple'>

a=98
b=66
print("A+B = ",a+b)
#Output: A+B = 164
print(f"A+B = {a+b}")
#Output: A+B = 164
print(f"{a}+{b} = {a+b}")
#Output: 98+66 = 164

val=9
if val > 9:
    print(f"{val} is greater than 9 ")
else:
    print(f"{val} is not greater than 9 ")
#Output: 9 is not greater than 9 

#w.a.p to compare two numbers
num_1 = int(input("Enter a number: ")) #Enter a number: 14
num_2 = int(input("Enter a number: ")) #Enter a number: 23
if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_1 == num_2:
    print(f"{num_1} is equal to {num_2}")
else:
    print(f"{num_1} is less than {num_2}")
#Output: 14 is less than 23

#EVAL FUNCTION -- eval()
val = eval(input("Enter the value: ")) #Enter the value: (1,2,3)
print(type(val))
#Output: <class 'tuple'>
print(val)
#Output: (1, 2, 3)

#w.a.p to check if their age is eligible to vote
age = int(input("Enter Your age: ")) #Enter Your age: 23
if age >=18:
    print("You are eligible to vote.")
else:
    print(f"You still have to wait for {18-age} years to vote.")
#Output: You are eligible to vote.
    
# w.a.p to display fail if less than 35 and pass if more than 35
marks = int(input("Enter Your marks: ")) #Enter Your marks: 45
if marks >= 35:
    print("You Passed!")
else:
    print("You Failed!")
#Output: You Passed!

