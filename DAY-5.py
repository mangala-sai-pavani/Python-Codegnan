'''

o Mutable:you can modify the original value in the variable as well as u can change the value it impacts the original value in
  variable.and when the variable is dispplayed it diplays the value with the changes done.
  ex: an = [1,2,3,4]
      an.append(76)
      print(an)
      #Output: [1, 2, 3, 4, 76]
      an.append([1,2,3,4,5])
      print(an)
      #Output: [1, 2, 3, 4, 76, [1, 2, 3, 4, 5]] 

o Immutable: you cannot modify the original value in the variable thou u can change the value n diplay right away but cannot impact
  the original value in variable.
  ex: var = "Python is a laungugae"
      print(var.replace("Python","Java"))
      #Output: Java is a laungugae
      print(var)
      #Output: Python is a laungugae
o Slicing: It is used to get the particular part of the list,string or tuple technically to access the values between the given
           index position
           - This works based on the index position.
           Syntax: variable_name[starting_index : ending_index]

o List - It is a collection of data types and it is represented by [] separated by comma
  ex: list_1 = [1,"Python",[34,9]]
      print(list_1)
      #Output: [1, 'Python', [34, 9]]
  - List Methods:
  o append(): It is used to add new item into list , but it will add in the last index position.
    Syntax: variable_name.append(item)
    - Note : -it can only consider one argument lets say a number or collection of values in the form of list.
             -it considers int values too.
  o extend(): It is used to add new item into list,but this extend() adds each position(charecter/value) to each index in the list.
    Syntax: variable_name.extend(item)
    - Note : It only considers iterables.
  o pop(): -It is used to delete an item from the list ,this pop()removes the value based on the index position mentioned in the
          parameters
         -If nothing is mentioned in the parameters , it will remove the value present in the last index position.
    Syntax: Syntax: variable_name.pop(index_value)
    - Note: it removes values based on index.
  o remove(): It is also used to delete item from the list, but remove() meethod will delete the value directly.
    Syntax: variable_name.remove(value)
  o len(): It is used to find the number of items present in the list.
     Syntax: len(variable_name)
  o index():
  o count():
  o insert(): 
'''
list_1 = [1,"Python",[34,9]]
print(list_1)
#Output: [1, 'Python', [34, 9]]

#print a charecter within the list using indexing
list_2 = [1,"Python is a language",[2,"this is 5th class",3],56]
print(list_2[2])
#Output: [2, 'this is 5th class', 3]
print(list_2[2][1])
#Output: this is 5th class
print(list_2[2][1][10])
#Output: h
list_3 = [1,"Python is a langugae",67,68,[34,["This is python class"],78,"I'm looking for a good bat"],[2,"this is a 5th class",3],56]
print(list_3[4])
#Output:[34, ['This is python class'], 78, "I'm looking for a good bat"]
print(list_3[4][1])
#Output: ['This is python class']
print(list_3[4][1][0])
#Output: This is python class
print(list_3[4][1][0][14])
#Output: (space)

var = "Python is a laungugae"
print(var.replace("Python","Java"))
#Output: Java is a laungugae
print(var)
#Output: Python is a laungugae

#append()
an = [1,2,3,4]
an.append(76)
print(an)
#Output: [1, 2, 3, 4, 76]
an.append([1,2,3,4,5])
print(an)
#Output: [1, 2, 3, 4, 76, [1, 2, 3, 4, 5]]

#append() & extend()
any = [1,2]
any.append([2,3])
print(any)
#Output: [1, 2, [2, 3]] 
any.extend([2,3])
print(any)
#Output: [1, 2, [2, 3], 2, 3] 
any.append("Python")
print(any)
#Output: [1, 2, [2, 3], 2, 3, 'Python'] 
any.extend("Python")
print(any)
#Output: [1, 2, [2, 3], 2, 3, 'Python', 'P', 'y', 't', 'h', 'o', 'n']

#pop()
list_4 = [1,2,3,4]
list_4.pop(2)
print(list_4)
#Output: [1, 2, 4]

#remove()
list_4 = [1,2,3,4]
list_4.remove(3)
print(list_4)
#Output: [1, 2, 4]

#Slicing
list_5 = [1,2,3,4,5,6,67,7,9,8]
print(list_5[3:6])
#Output: [4, 5, 6]

#len()
str_1 = "Python is a language"
print(len(str_1))
#Output: 20
