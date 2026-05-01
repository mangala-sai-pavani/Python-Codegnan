'''
o elif statement -> It gives more options to get the result of the program.
ex:
#grade system
marks = int(input("Enter Marks: ")) #Enter Marks: 78
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C+")
else:
    print("Fail")
#Output: B+

o nested if statement -> it refers to an if statement within another if statement,called as nested if statement.
ex:
#ATM PIN check

user_SBI_info = {"ATM PIN":"1984"}
user_pin = input("Enter your pin: ")
if len(user_pin)==4:
    if user_pin in user_SBI_info["ATM PIN"]:
        print("Welcome to SBI ATM.")
    else:
        print("Please enter the correct pin.")
else:
    print("Please enter 4 digit pin.")

#Output-1:
Enter your pin: 45678
Please enter 4 digit pin.
#Output-2:
Enter your pin: 1984
Welcome to SBI ATM.

o for statement -> It is used to iterate over items like(string,list or tuple) with fixed number of iterations.
ex:
#for loop

val = [23,45,67,89]
for j in val: # j is a temporary variable or an instance
    print(j)

#Output:
23
45
67
89

o else statement in for loop --> after the completion of iterations , the else statement will execute.
ex:
#for loop

val = [23,45,67,89]
for j in val: # j is a temporary variable or an instance
    print(j)
else:
    print("Loop finished.")

#Output:
23
45
67
89
Loop finished.

o while statement --> it will iterate until the given condition is true.
'''
#grade system
marks = int(input("Enter Marks: ")) #Enter Marks: 78
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C+")
else:
    print("Fail")
#Output: B+


#ATM PIN check

user_SBI_info = {"ATM PIN":"1984"}
user_pin = input("Enter your pin: ")
if len(user_pin)==4:
    if user_pin in user_SBI_info["ATM PIN"]:
        print("Welcome to SBI ATM.")
    else:
        print("Please enter the correct pin.")
else:
    print("Please enter 4 digit pin.")
'''
#Output-1:
Enter your pin: 45678
Please enter 4 digit pin.
#Output-2:
Enter your pin: 1984
Welcome to SBI ATM.
'''

#for loop

val = [23,45,67,89]
for j in val: # j is a temporary variable or an instance
    print(j)
else:
    print("Loop finished.")
'''
#Output:
23
45
67
89
Loop finished.
'''

#string reverse

val = "Penelope Echkart"
val_1 = ""
empty_val = ""
for i in val:
    val_1 += i
    empty_val = i+empty_val
print(val_1)
print(empty_val)
#Output-1: Penelope Echkart
#Output-2: trakhcE epoleneP

#palindrome
val = "madam"
empty_val = ""
for i in val:
    empty_val = i+empty_val
if empty_val == val:
    print(f"{val} is a palindrome.")
else:
    print(f"{val} is not a palindrome.")
#Output-1: madam is a palindrome. 
