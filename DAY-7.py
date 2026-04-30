'''
o set: It is a collection of unordered elements or unique elements unlike list or tuple set is not permit duplicates in side.
       - represented by {}
  -Methods :
   o add() -> It is used to add new item into the set.
     syntax: variable_name.add(item)
     note: can only add single item no 2 arguments or {a,b} or duplicate can be added but a tuple can be added.
   o remove() -> It is used to delete an item in the set.
     synatx: variable_name.remove(value)
   o pop() ->It is used to delete element in the set ,but we cannot specify the element.
     synatx: variable_name.pop(no arguments)
     note: pop() in list removes element at the specified index position while pop() in set doesnt take any arguments n
     removes value of its choice
   o clear() -> It is used to delete all elements in the set.
     syntax: variable_name.clear()
   o update() -> It is similar to add() but it can add more than one element.
     syntax: variable_name.update([elements])
   o union() -> It returns a set with all elements from both sets but ignores the duplicate values.it can also be represented by '|'.
     syntax: set_1.union(set_2) or set_1 | set_2
   o intersection() -> It will return only the common elements from both the sets.
     syntax: set_1.intersection(set_2) or set_1 & set_2
   o difference() -> It is used to get different elements from both the sets.
     syntax: set_1.difference(set_2) or set_1 - set_2

o Type Conversions:Converting one data type into another data type.

'''
set_1 = {1,2,3,6}
set_2 = {9,10,11}
print(set_1.add(4))
#Output: None
print(set_1)
#Output: {1, 2, 3, 4, 6}
print(set_1.remove(2))
#Output: None
print(set_1)
#Output: {1, 3, 4, 6}
print(set_1.pop())
#Output: 1
print(set_1)
#Output: {3, 4, 6}
print(set_1.clear())
#Output: None
print(set_1)
#Output: set()
print(set_1.update([6,7,8]))
#Output: None
print(set_1)
#Output: {8, 6, 7}
print(set_1.union(set_2))
#Output: {6, 7, 8, 9, 10, 11}
print(set_1 | set_2)
#Output: {6, 7, 8, 9, 10, 11}
print(set_1.intersection(set_2))
#Output: set()
print(set_1 & set_2)
#Output: set()
print(set_1.difference(set_2))
#Output: {8, 6, 7}
print(set_1 - set_2)
#Output: {8, 6, 7}

#int -> str,float
a=8
b=str(a)
c=float(a)
print(a,b,c)
#Output: 8 8 8.0
print(type(a),type(b),type(c))
#Output: <class 'int'> <class 'str'> <class 'float'>

#float -> str,int
a=80.8
b=int(a)
c=str(a)
print(a,b,c)
#Output: 80.8 80 80.8
print(type(a),type(b),type(c))
#Output: <class 'float'> <class 'int'> <class 'str'>

#str -> float,int(can only convert if string contains only int values),list,tuple
a="80" #check more examples of this 
b=int(a)
c=float(a)
l=list(a)
t=tuple(a)
print(a,b,c,l,t)
#Output: 80 80 80.0 ['8', '0'] ('8', '0')
print(type(a),type(b),type(c),type(l),type(t))
#Output: <class 'str'> <class 'int'> <class 'float'> <class 'list'> <class 'tuple'>

#list to str,tuple
li = [1,2]
b=str(li)
t= tuple(li)
print(li,b,t)
#Output: [1, 2] [1, 2] (1, 2)
print(type(li),type(b),type(t))
#Output: <class 'list'> <class 'str'> <class 'tuple'>

#task -convert str to int n perform mathematical operations.
