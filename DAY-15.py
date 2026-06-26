'''
#lamda() :
-->It is a small anonymouos function.
--> This fn can take n number of arguments but can only have one expression.
--> also known as anonymous fn and its a one line syntax.
o syntax: lambda keyword (arguments) : (expression)
ex:
an = lambda a,b : a+b
print(an(5,6))#11

bc = lambda c,d : c**d
print(bc(8,9)) #134217728

even = lambda c : c if c%2==0 else "Not even"
print(even(8))

#Fibonacci
num=0
num_1 = 1
any_ = int(input("Enter a number: ")) #Enter a number: 5
print(num,num_1,end=" ")
for i in range(1,any_+1):
    num_2 = num+num_1
    num=num_1
    num_1 = num_2
    print(num_2,end=" ")
#Output: 0 1 1 2 3 5 8

#Amstrong
n = int(input("Enter a number: ")) #Enter a number: 153
total = 0
l = len(str(n))
for i in str(n):
    total+=int(i)**l
if n == total:
    print(f"{n} is an amstrong number.")
else:
    print(f"{n} is an amstrong number.")
# Output: 153 is an amstrong number.

# w.a.p to find the numbers divisible by 3 and 5
num = int(input("Enter a number: ")) #Enter a number: 45
if num%3==0 and num%5==0 or num%15==0:
    print(f"{num} is divisible by 3 and 5.")
else:
    print(f"{num} is divisible by 3 and 5.")
# Output: 45 is divisible by 3 and 5.

#generate seq of numbers till certain range that ae divisible by both 3 and 5

n=int(input("Enter the number till u want the sequence: ")) #Enter the number till u want the sequence: 100
for i in range(1,n+1):
    if i%3==0 and i%5==0 or i%15==0:
        print(f"{i} is divisible by 3 and 5.")

Output:
Enter the number till u want the sequence: 100
15 is divisible by 3 and 5.
30 is divisible by 3 and 5.
45 is divisible by 3 and 5.
60 is divisible by 3 and 5.
75 is divisible by 3 and 5.
90 is divisible by 3 and 5.

# sum of all even numbers and odd numbers #enter the limit: 100
n = int(input("enter the limit: "))
eve = 0
odd = 0
for i in range(1,n+1):
    if i%2==0:
        eve+=i
    else:
        odd+=i
print(f"Sum of even numbers till {n} is {eve}")
print(f"Sum of odd numbers till {n} is {odd}")
Output:
Sum of even numbers till 100 is 2550
Sum of odd numbers till 100 is 2500

#w.a.fn to calc sum of all even numbers in given datatype.
any = eval(input("")) # it iterates each element in loop without range fn
def sum_even(any):
    total = 0
    for i in any:
        if i % 2==0:
            total+=i
    print(total)
sum_even(any)
Output: {1,2,3,5,6}
8
'''
    
