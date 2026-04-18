'''
Data Types
 - data -> information of a particular data 
 - type -> what kind of data it is

 - TYPES OF DATATYPEs:
    o Mutable   - can be modified directly on the variable , which the data type have taken.
                  (value stored in the variable can be modified)
                  ex: List , Dictionary (dict)
    o Immutable - cant be modified directly on the variable assigned to the data type.
                  (value stored in the variable cant be modified)
                  ex: int , string 

o integer or int:
 - Storing number or digit in the variable is called int.
   ex: num_2 = 89
o float:
 - storing decimal values in the variable is called float.
   num_3 = 67.98
o indexing:
    - used to get particular substring , item from string , list and tuple.
    - it begins from 0 , it also counts space
    - if used index() -> it returns the index of the 1st charecter's index
    syntax: variable_name[index_position] -> to find the charecter at the index position.
            variable_name.index("charecter")
o concatenation:
    - it is used to  combine two strings or lists
    - a '+' acts in different ways , if we are adding 2 integers , it acts like addition
      In other cases such as list , string and tuple it acts like concatenation.
      ex: 
          num_ = 2
          num__ = 4
          print(num_ + num__)
          #Output:6
          str_ = "string"
          str__ = "value"
          print(str_ + str__)
          #Output:stringvalue
          list_ = [9 , 0]
          list__ = [10 , 87]
          print(list_ + list__)
          #Output:[9, 0, 10, 87]

o string or st  r:
  - string is a collection of charecter(char) that are enclosed in '' , "" , ''''''.
  - it is immutable data type.
  - can be changed can't be modified
  
  o methods:
   - replace() -> This method is used to replace or change old sub string with new string
     syntax: variable_name.replace("old_string" , "new_string")
   - split() -> This method is used to seperate the string using a substring and it will
                split into list such as before the substring is one index and after the
                substring is another index.
     syntax: variable_name.split("substring")
   - strip() -> This method is used to remove from 1st index position or from last index position.
     syntax: variable_name.split("charecter of 1st or last index position")
   - join() ->
     syntax: substring.join(variable_name))
   - lower() ->
     syntax:
   - count() ->
   - capitalize() ->
   - casefold() ->
   - isalnum() ->
   - isalpha() ->
   - isdigit() ->
   - isdecimal() ->
   - islower() ->
   - isupper() ->
o Doc String:(f"{var_name} and any desired statements.")
             ex:num=int(input("Enter number: "))
             print(f"{num} is even number.")
     
'''
num_1 = 87
num_2 = 76
print(num_1 + num_2)
print(num_1)
print(num_2)

'''Output:
163
87
76
'''

#INDEXING
any = ("Python is a programming language.")
print(any[14])
#Output:o
print(any.index("o"))
#Output: 4
print(any[9])
#Output:  (space)

#CONCATENATION
num_ = 2
num__ = 4
print(num_ + num__)
#Output:6
str_ = "string"
str__ = "value"
print(str_ + str__)
#Output:stringvalue
list_ = [9 , 0]
list__ = [10 , 87]
print(list_ + list__)
#Output:[9, 0, 10, 87]

#replace()
any = ("Python is a programming language.")
print(any.replace("Python" , "Java" ))
#Output: Java is a programming language.
print(any)
#Output: Python is a programming language.
print(any.replace(" " , "_"))
#Output: Python_is_a_programming_language.

#split()
print(any.split(" "))
#Output: ['Python', 'is', 'a', 'programming', 'language.']
print(any.split("a"))
#Output: ['Python is ', ' progr', 'mming l', 'ngu', 'ge.']

#strip()
print(any.strip("P"))
#Output: ython is a programming language.
print(any.strip("age."))
#Output: Python is a programming langu

#join()
print('-'.join(any))
#Output: P-y-t-h-o-n- -i-s- -a- -p-r-o-g-r-a-m-m-i-n-g- -l-a-n-g-u-a-g-e-.

#lower()
print(any.lower())
#Output:python is a programming language.

#Doc String
num=int(input("Enter number: "))
print(f"{num} is a number.")
#Output: 345 is a number.
