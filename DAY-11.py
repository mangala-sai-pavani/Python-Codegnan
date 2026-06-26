'''
PATTERN PROGRAMS:
----------------

#print a right angled triangle using stars.
num = int(input("Enter a number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")#end is used to print in same line
    print("")# basically to end that loop so it moves to the next line
#or
for k in range(1,num+1):
    print("*"*k)
#both the programs give the same output

'''
'''Output:
Enter a number: 5
*
**
***
****
*****
'''
'''
#print a right angled triangle using numbers.
num = int(input("Enter a number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")

'''
'''Output:
Enter a number: 4
1
12
123
1234
'''
'''
#print a reverse right angled triangle using stars.
num = int(input("Enter a number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print("")

'''
'''Output:
Enter a number: 5
*****
****
***
**
*
'''
'''
#print a reverse right angled triangle using numbers.
num = int(input("Enter a number: "))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print("")

'''
'''Output:
Enter a number: 5
12345
1234
123
12
1
'''
'''
#print a pyramid using stars.

num=int(input("Enter a number: "))
for i in range(num):
    for j in range(num-i-1,0,-1):
        print(" ",end="")#to place the cursor at the desired position
    for k in range(i+1):
        print("* ",end="")# space is must cuz only then it will be displayed as pyramid
    print()
'''   
'''Output:
Enter a number: 5
    * 
   * * 
  * * * 
 * * * * 
* * * * *
'''

#basic calculator
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
choice =int(input("\n1. Add \n2. Subtract \n3. Multiply  \n4.Divide \n5.Power \n6.Exit \n\nEnter your choice: "))
if choice ==1:
    print(num_1+num_2)
elif choice ==2:
        print(num_1-num_2)
elif choice ==3:
        print(num_1*num_2)
elif choice ==4:
        print(num_1/num_2)
elif choice ==5:
        print(num_1**num_2)
elif choice ==6:
        exit()

