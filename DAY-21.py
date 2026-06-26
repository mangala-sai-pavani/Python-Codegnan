'''
o class:
-----
-->

o object:
------
-->object is an instance of a class.
ex:
class car:
    def brand(self):
        print("I have created aa new car.")
car_1 = car()
car_1.brand()

o Constructor:
--------------
--> A constructor is a speecial method that executes automatically when the object is created.
--> a class has only one constructor.
--> ex: (__init__)
class car:
    def __init__(self,color,Brand,Model):
        self.color = color
        self.Brand = Brand
        self.Model = Model

    def car_brand(self):
        print(f"Brand is {self.Brand}")
        #print(f"Model is {self.Model}")

    def car_color(self):
        print(f"Color is {self.color}")

    def car_model(self):
        print(f"Model is {self.Model}")

Car_1 = car("Blue","BMW","M-series")
Car_1.car_brand()

o self keyword:
---------------
-->this refers to the current object.
ex:
class student:
    def __init__(self,name,age,gender,year):
        self.name = name
        self.age = age
        self.gender = gender
        self.year = year
    def student_details(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.year)
    def student_year(self):
        print(self.year)

stu = student("Pavani",20,"Female",2026)
stu.student_details()
stu.student_year()

o Access Specifiers:
--------------------

Types:

 -Public
 -Private -> __ is used to represent a pvt variable.
 -Protected -> _ is used to represent a protected variable.
ex:
class student:
    def __init__(self,name,age,gender,year):
        self.name = name
        self.__age = age #pvt variable
        self._gender = gender #protected variable
        self.year = year
    def student_details(self):
        print(self.name)
        print(self.__age)
        print(self._gender)
        print(self.year)
    def student_year(self):
        print(self.year)

stu = student("Pavani",20,"Female",2026)
stu.student_details()
stu.student_year()

o Encapsulation:
----------------
-->This binds data and the methods that works on the data inside the class,while limiting direct access to the internal state.

name is public and can be accessed directly.
Aadhar is protected,means internal use only
Pan is a private,this makes direct access hard
ex:
class bank:
    def __init__(self,name,Aadhar,Pan):
        self.name = name
        self._Aadhar = Aadhar
        self.__Pan = Pan
    def Aadhar(self):
        print(self._Aadhar)
    def Pan(self):
        print(self._Pan)
SBI_bank = bank("Sai Pavani",643164316431,"ABJI65789PK")
SBI_bank.Aadhar()
l
'''
'''
class animal:
    def __init__(self,breed,color,age,sound,animal_type):
        self.breed = breed
        self.color = color
        self.age = age
        self.sound = sound
        self.animal_type = animal_type

    def dog(self):
        
        print(self.breed)
        print(self.color)
        print(self.age)
        print(self.sound)
        print(self.animal_type)

    def cat(self):
        
        print(self.breed)
        print(self.color)
        print(self.age)
        print(self.sound)
        print(self.animal_type)

    def fox(self):
        
        print(self.breed)
        print(self.color)
        print(self.age)
        print(self.sound)
        print(self.animal_type)
animal_1 = animal("Labrador","Golden",3,"Bark","Domestic")
animal_2 = animal("Persian","White",2,"Meow","Domestic")
animal_3 = animal("Red Fox","Reddish Orange",1,"Screech","Wild")
animal_1.dog()
animal_2.cat()
animal_3.fox()
'''
