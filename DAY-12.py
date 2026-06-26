'''  
#removing duplicate values from list
numbers = eval(input("Enter items of list : ")) #Enter items of list : 1,2,3,3,4,5
empty=[]
for i in numbers:
    if i not in empty:
        empty.append(i)
print(empty)
# Output: [1, 2, 3, 4, 5]

nums = [10,2,20,76,4,4,99]
max1 = 0
max2 = 0
for num in nums:
    if num>max1:
        max2 = max1
        max1=num
print(f"{max2} is the max number in the list  {nums}")
# Output: 76 is the max number in the list  [10, 2, 20, 76, 4, 4, 99]
''' 
pavani_SBI_AC_details = {"Name":"Pavani",
                         "ATM PIN":"1984",
                         "Balance":9000}
print("WELCOME TO SBI ATM")
print("Please enter your card ")

