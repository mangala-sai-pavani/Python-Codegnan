'''
Recursive function: It calls itself until a base case is stops it.


def Fact(num):
    if num == 0 or num ==1 :
        return 1
    return num*Fact(num-1)
print(Fact(6))
#Output: 720
'''
def table(num):
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}")
num=int(input("Enter a number: "))
table(num)
        
