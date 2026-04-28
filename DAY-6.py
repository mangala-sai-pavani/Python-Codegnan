'''
o Tuple -> It is a collection of different data types that are represented by '()' and items in the tuple is separated by comma.
        -> it is immutable.
        ex: tup_1 = (1,"Python",[7,8],(4,7))
        tup_2 = (56,8,9,0)
        print(tup_1+tup_2)
        #Output: (1, 'Python', [7, 8], (4, 7), 56, 8, 9, 0)

o Dictionary -> It is a collection of key - value pairs separated by ':',where keys are immutable(string,int,tuple)
                and values can be of any data type.
                - cant contain duplicate keys if it has it considers the latest occurence.
  o Methods :
            -keys() -> It is used to access only the keys of the dictionary.
             syntax: dictionary_name.keys()
             ex: print(dict_1.keys())
             #Output: dict_keys(['name', 'age', 'education'])
            -values() -> It is used to access only the values of the dictionary.
             syntax: dictionary_name.values()
             ex: print(dict_1.values())
             #Output: dict_values(['pavani', 20, 'BSc'])
            -items() -> It is used to access key-value pair in the dictionary.
             syntax: dictionary_name.items()
             ex: print(dict_1.items())
             #Output: dict_items([('name', 'pavani'), ('age', 20), ('education', 'BSc')])
             NOTE: in operator is used to check if a string value is present in the dictionary.
            -clear() -> It is used to delete all the items in the dictionary.
             syntax: dictionary_name.clear()
            -update() -> It is used to add new item(key-value pair) into the dictionary.
             syntax: dictionary_name.update({key:value})

'''
#TUPLE
tup_1 = (1,"Python",[7,8],(4,7))
tup_2 = (56,8,9,0)
print(tup_1+tup_2)
#Output: (1, 'Python', [7, 8], (4, 7), 56, 8, 9, 0)

#DICTIONARY

dict_1 = {"name" : "pavani",
          "age" : 20,
          "education" : "BSc"}
print(dict_1)
#Output: {'name': 'pavani', 'age': 20, 'education': 'BSc'}
print(dict_1.keys())
#Output: dict_keys(['name', 'age', 'education'])
print(dict_1.values())
#Output: dict_values(['pavani', 20, 'BSc'])
print(dict_1.items())
#Output: dict_items([('name', 'pavani'), ('age', 20), ('education', 'BSc')])
print("pavani" in dict_1["name"])
#Output: True
dict_1.update({"role":"Python Developer"})
print(dict_1)
#Output: 
