'''
o LIST COMPREHENSION
---------------------
-> It offers shorter syntax when we want to crerate a new list based
on the values of an existing list.
o syntax: [expression loop condition] 
ex:
old_l = [12,34,56,78,90]
new_l = [i for i in old_l if i%2==0]
print(new_l)
#o/p: [12, 34, 56, 78, 90]

#list comprehension using if else in a loop
old_l = [12,34,56,78,90,5]
new_l = [i if i%2==0 else "odd" for i in old_l]
print(new_l)
#o/p: [12, 34, 56, 78, 90, 'odd']

#list comprehension using if else in a loop
old_l = [12,34,56,78,90,5]
new_l = [i if i%2!=0 else "even" for i in old_l]
print(new_l)
#o/p: ['even', 'even', 'even', 'even', 'even', 5]

o Dictionary Comprehension
--------------------------
--> It offers shorter syntax when we want to create a new dictionary based 
on the values of an exising dictionary.
o syntax: {expression loop conditon}


dict_1= {"a": 1,"b": 2,"c":1}
dict_2 = {x:y for (x,y) in dict_1.items()}
print(dict_2)
#o/p: {'a': 1, 'b': 2, 'c': 1}

dict_1= {"a": 1,"b": 2,"c":1}
dict_2 = {x:y for (x,y) in dict_1.items() if y%2==0}
print(dict_2)
#o/p: {'b': 2}
'''