'''
o Single Inheritance:
--> A child class inherits from one base class

class animal:
   def sound(self):
      print("Animals make soounds.")
class dog(animal):
   def bark(self):
      print("Dog Bark")
d=dog()
d.sound()
d.bark()

o Multiple Inheritance:
-->A child class inherits more than one class.
ex:
class Father:
    def skill_1(self):
        print("Driving")
class Mother:
    def skill_2(self):
        print("Cooking")
class child(Father,Mother):
    def All_skills(self):
        print("Coding")
c=child()
c.skill_1()
c.skill_2()
c.All_skills()
ex:
class Aptitude:
    def aptitude(self):
        print("Aptitude")
class Python:
    def python(self):
        print("Python Language")
class Softskills:
    def soft_skills(self):
        print("Soft Skills")
class Student(Aptitude,Python,Softskills):
    def student(self):
        print("Learning")
s = Student()
s.aptitude()
s.python()
s.soft_skills()
s.student()

o Multi-Level Inheritance:
--> inherits from another child class
ex:
class grandfather:
    def house(self):
        print("Grandfather's House")
class father(grandfather):
    def land(self):
        print("Father's land")
class son(father):
    def flat(Self):
        print("Son's flat")
s = son()
s.house()
s.land()
s.flat()

o Hierarchial Inheritance:
--> multiple child classes inherits from one base class.

class father:
    def property(self):
        print("Father's Property")
class child_1(father):
    def car(self):
        print("Child one's car")
class child_2(father):
    def flat(self):
        print("Child two's flat")
c1 = child_1()
c2 = child_2()
c1.car()
c1.property()
c2.flat()
c2.property()

o Hybrid Inheritance:
--> combination of types of inheritance.
ex:
class A:
    def method_A(self):
        print("Class A")
class B(A):
    def method_B(self):
        print("Class B")
class C(A):
    def method_C(self):
        print("Class C")
class D(B,C):  #multiple heritance
    def method_D(self):
        print("Class D")
d = D()
d.method_A()
d.method_B()
d.method_C()
d.method_D()

o super() method:
--> to access parent class or call the methods or constructor from parent class
'''
class parent:
    def __init__(self):
        print("Parent Constructor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")
c = child()
