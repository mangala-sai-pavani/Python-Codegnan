'''
*Operators :
 - Types of Operators :
  o Arthimetic Operators : +,-,%,*,**,/,//
  o Assignment Operators : =,+=,-+,*=,//=,**=,&=
  o Comparison operators : ==,!=, >,<,>=,<=
  o Logical Operators :
    - and : the 2 conditions should be True then only the output would be True
    - or  : if one of the condition is True the output would be True
    - not : to reverse the output
  o Identity Operator :
    - is     : is used to check to the object (based on location of that variable) 
    - is not : is used to check to the object (based on location of that variable)
  o Membership Operator :
    - in     : to check if its present in it
    - not in : to check if its  not present in it
  o Bitwise Operator :
    &,|,^,~,<<,>>
*NOTE:
 o the difference between is and == is that == checks if both the given variables are equal or not
   while is checks the object(memory loaction) if same returns True
'''
#Arthimetic Operator (+)
number_1=68
number_2=89
number_3=76
print(number_1+number_2+number_3)
#Output: 233
#Arthimetic Operator (-)
num_1 = 76
num_2 = 98
print(num_1 - num_2)
#Output: -22
#Arthimetic Operator (%)
n_1 = 77
n_2 = 6
print(n_1 % n_2)
#Output: 5
#Arthimetic Operator (*)
numm_1 = 67
numm_2 = 5
print(numm_1 * numm_2)
#Output: 335
#Arthimetic Operator (**)
numb_1 = 6
numb_2 = 5
print(numb_1 ** numb_2)
#Output: 776
#Arthimetic Operator (//)
digit_1 = 63
digit_2 = 5
print(digit_1 // digit_2)
#Output: 12
digit_3 = 63.987
digit_4 = 52.9
print(digit_3 // digit_4)
#Output: 1.0

#Assignment Operator
# = --> used to assign a value
digi = 87
digi += 1
digi1 = 87
digi1 = digi1 +1
print(digi,digi1)
#Output: 88 88
digi2 = 76
digi2 -= 6
print(digi2)
#Output: 70
digi3 = 64
digi3 *= 2
print(digi3)
#Output: 128
digi4 = 5
digi4 **=4
print(digi4)
#Output: 625
digi5 = 86.947
digi5 //= 6
print(digi5)
#Output: 14.0

#Comparison Operator
# --> Used To Compare variables
dig1=34
dig2=65
print(dig1 == dig2)
#Output: False
print(dig1 != dig2)
#Output: True
print(dig1 > dig2)
#Output: False
print(dig1 < dig2)
#Output: True
print(dig1 >= dig2)
#Output: False
print(dig1 <= dig2)
#Output: True

#Logical Operator
# and operator
di_1 = 4
d1_2 = 9
print(di_1 > 5 and di_2 < 10)
#Output: False 
#or operator
di_3 = 6
di_4 = 80
print(di_3 > 10 or di_4 <100)
#Output: True
#not operator
di_5 = 7
di_6 = 8
print(not(di_3 > 10 or di_4 <100))
#Output: False

#Identity Operator
#is
d1 = 23
d2 = 23
print(d1 is d2)
print(id(d1))
print(id(d2))
'''Output:
True
140716081784632
140716081784632'''
list_ = [1,2]
list_2 = [1,2]
list_3 = list_
print(list_ is list_2)
print(id(list_))
print(id(list_2))
print(id(list_3))
'''Output:
False
2419013054976
2419069139200
2419013054976
'''
#is not
d3 = 23
d4 = 23
print(d3 is not d4)
print(id(d3))
print(id(d4))
'''Output:
False
140716081784632
140716081784632
'''
list_4 = [1,2]
list_5 = [1,2]
list_6 = list_4
print(list_4 is not list_5)
print(list_4 is not list_6)
print(id(list_4))
print(id(list_5))
print(id(list_6))
'''Output:
True
False
2192021895232
2192021895616
2192021895232
'''

#Membership Operator
#in 
list__ = [1,2,4]
print(4 in list__)
#Output:True

#not in
print(6 not in list__)
#Output: True

#Bitwise Operator
# & - Bitwise AND (addition)
'''
CALCULATIONS:
------------

5 -> 0101
3 -> 0011
---------
1 -> 0001
---------

6 -> 0110
8 -> 1000
---------
0 -> 0000
---------
'''
print(5 & 3)
#Output: 1
print(6 & 8)
#Output: 0

# | - Bitwise OR ()
'''
CALCULATIONS:
------------

5 -> 0101
3 -> 0011
---------
7 -> 0111
---------

6 -> 0110
8 -> 1000
---------
 14 -> 1110
---------
'''
print(5 | 3)
#Output: 7
print(6 | 8)
#Output: 14


# ^ - Bitwise XOR
'''
CALCULATIONS:
------------

5 -> 0101
3 -> 0011
---------
6 -> 0110
---------

6 -> 0110
8 -> 1000
---------
 14 -> 1110
---------
'''
print(5 ^ 3)
#Output: 6
print(6 ^ 8)
#Output: 14





