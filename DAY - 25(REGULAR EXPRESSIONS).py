"""
o Regular Expressions:
-->
ex:

o Meta Characters: 
--> using "." -> reps a single character.
ex:
import re
some = "Python is a language"
any = re.findall("P..h..",some)
print(any)

--> using "^" -> sees if the given string is starting with or not.
ex:
import re
some = "Python is a language"
any = re.findall("^P",some)
print(any)

--> using "$" -> checks if given sequence is the ending string in original string.
ex:
import re
some = "Python is a language"
any = re.findall("language$",some)
print(any)

--> using "*" -> 0 to n no.of characters
-->considers the last occurence of the given character
ex:
import re
some = "Python is a language"
any = re.findall("P.*",some) # the . lets the * consider the whole string.
print(any)

--> using "+" -> 1 to n characters
--> atleast one character should form a searching pattern.
ex:
import re
some = "Python is a language"
any = re.findall("P.+hon",some) # the . lets the + consider the whole string.
print(any)

-->using "{}" -> we specify no.of characters
--> forms the pattern based on the size specified in {}
"""
import re
some = "Python is a language"
any = re.findall("P.{10}",some) # the . lets the {} consider the whole string till specified range.
print(any)
