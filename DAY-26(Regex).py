'''Regex'''
import re

def name_validate(name):
    pattern = "^[A-za-z]+$"
    if re.fullmatch(pattern,name):
        print("Valid Name")
    else:
        print("Invalid name , must begin with a capital letter")

def phone_number_validate(phno):
    pattern = r'^[6-9]\d{9}$'
    if re.fullmatch(pattern,phno):
        print("Valid Phone Number , must have digits and 10 numbers")
    else:
        print("Invalid Phone Number")
def email_validate(email):
    pattern = r"^[a-z0-9]+@+[]"

def password_validate(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@!$%&])[A-Za-z\d@!$%&]{8,16}$'
    if re.fullmatch(pattern,password):
        print("Valid Password")
    else:
        print("Invalid Password,must have a capital letter,a number, a special charecter and must be 8-16 character long.")

name= input()
phno = input()
password = input()
name_validate(name)
phone_number_validate(phno)
password_validate(password)
