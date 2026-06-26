'''#email authorization
dict_1 = {"name":"sai pavani","email":"saipavani079@gmail.com","phone number":8985957353}
email = input("Enter your email: ")#Enter your email: saipavani079@gmail.com
if dict_1["email"] == email:
    print("Login Successful.")
else :
    print("Login Failed. You are unauthorised")
#Output: Login Successful.

#add common elements n add to new list
list_1 = [12,67,5,3,7]
list_2 = [5,7,56]
list_3 = []
for i in list_1:
    for j in list_2:
        if i == j:
            list_3.append(j)
print(list_3)
#Output: [5, 7]
'''
#print the list with nested lists as a single list
an = [1,[2,3],[4,[5,6]],7,[[8]]]
print(flatten(an))

