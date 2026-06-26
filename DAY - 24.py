"""
File Handling:
-------------
-->File handler is an object of a file to maintain several functions of file like
creating,reading,updating and deleting the file

o Ways to open a file:
-> open():
syntax:
file_handler = open("file_name.txt","mode")
rest of the code...
file_handler.close()
ex:
f = open("file_handling.txt","r")
print(f.read())
f.close()
-> with open():
syntax:
with open("file_name","mode") as file_handler:
     code.....
ex:
with open("file_handling.txt","r") as f:
     print(f.readlines())

o with keyword:
--> by using it there wont be any need to close the file it closes the file automatically.

o Modes:
--------
- r --> used to read the file and will throw an error if the file doesnt exist.
- a --> used to add the text at the end, if the file doesnt exist it will create a file.
- w --> used to overwrite the existing text with new text,if the file doesnt exist it will create a file.
- x --> used to create the file and write text into the file,throws an error if file exist.
ex:
with open("ris.txt","x") as f:
    print(f.write("Ris"))
with open("file_handling.txt","r") as f:
    
    #print(f.readline())
    #print(f.readlines())
    print(f.read())
with open("ris.txt","a") as g:
    print(g.write("You make ordinary moments feel safe and beautiful."))
with open("strahl.txt","w") as h:
    print(h.write("You feel like home in the quietest and safest way possible. Being around you makes everything feel softer, calmer, and easier to carry. You have this gentle kindness that makes people feel understood without needing to explain themselves. Your presence feels like peace after a long exhausting day, like warmth during heavy rains, like finally being able to breathe properly again. You make ordinary moments feel special just by being there, and somehow the world feels less harsh when it is with you."))
with open("hoshi.txt","x") as i:
    print(i.write("Some people bring excitement, but you bring peace. You have the kind of presence that makes hard days feel lighter and silence feel comforting instead of empty. Being with you feels natural, safe, and warm, like finding a place my heart can finally rest in. Your kindness is quiet but unforgettable, the kind that stays with people long after the moment passes."))


o read types:
- read():
--> It reads the entire file chunk by chunk where we can specify the size.
ex:
with open("file_handling.txt","r") as f:
    print(f.read(56))

- readline():
--> It reads one line at a time.
ex:
with open("file_handling.txt","r") as f:
    print(f.readline())
- readlines():
--> it returns a list of all the lines in a file.
ex:
with open("file_handling.txt","r") as f:
    print(f.readlines())

--> note : for "w" and "a" mode we will use write() method
"""

