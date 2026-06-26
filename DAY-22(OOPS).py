'''
o POLYMORPHISM:
---------------
--> Polymorphism means many forms. The same method ,operator or a function
can perform different actions depending upon the object or datatype.

1. Method Overloading:
----------------------
-->Method overloading is creating multiple methods with the same name but different parameters
ex: multiple method with diff data
class Addition:
    def add(self,a,b=0,c=0):
        return a+b+c
    def add(self,a,b=0,c=0,d=0):
        return a+b+c+d
obj = Addition()
print(obj.add(23,7))
print(obj.add(10,20,30,9))

ex:
class Addition:
    def add(self,a,b=0,c=0):
        return a+b+c
obj = Addition()
print(obj.add(23,7))
print(obj.add(10,20,30))

ex:
class Power:
    def power(self,a,b=2):
        return a**b
p1 = Power()
print(p1.power(5))
print(p1.power(2,3))


2. Method Overriding:
---------------------
--> Method overriding occurs when the child class provides a different implementation of
a method that is already presnt in the parent class.
ex:
class animal:
    def sound(self):
        print("Animals make sound.")
class dog(animal):
    def sound(self):
        print("Dog barks.")
any = dog()
any.sound()
3. Operator Overloading:
------------------------
'''
class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,any_):
        return self.marks +any_.marks
so = student(56)
how = student(78)

print(so+how)
