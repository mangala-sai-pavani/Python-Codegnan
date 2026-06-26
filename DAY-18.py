'''
MODULES:
-> It is a file containing python code such as :
- variables
- functions
- classes

o Types:
 - User-defined: ex: demo_module,display_module
  ex:
import demo_module,display_module
#from math import sqrt --> isnt working in idle

print(demo_module.pow(2,4)) #16
print(demo_module.add(2,4)) #6
print(demo_module.prod(21,4))#84
print(demo_module.div(20,4)) #5.0
print(demo_module.mod(242,4))#2
print(display_module.module1())#This is module 1. None
print(display_module.hello_world())#Hello World! None
 - built-in: ex: os,sys,math

- to use all these modules,we have to import with the module
name using import keyword

o ways to import modules:
  1. using Alias name -> import module_name as alias_name
  ex: import pandas as pd
  2. import entire module -> import module_name
  ex: import pandas
  3. import all function -> from module_name import *
  ex: from pandas import *
  4. import specific function -> from module_name import function_name1,fn_name2
  ex: from math import sqrt

o math module:
ex:
import math
print(math.sqrt(196))#14.0
print(math.pow(2,5))#32.0
print(math.tan(45))#1.6197751905438615

o sys module: it is system-specfic parameters and functions.
ex:
import sys
print(sys.version) #3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]
print(sys.path)#['D:/CODEGNAN'
'''







