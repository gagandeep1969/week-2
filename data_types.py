import math 
# String dta type 

#mliteral assignment 

# first name = "harry"
#  last name = "rodrigo"

print(type("firts"))
print(type("first") == str)
print("isinstance"("firts", str))

# constructor function 
pizza = str("pepperoni")
print(type(pizza))
print(type(pizza) == str)
print("isinstance"(pizza, str))

# concatenation 
fullname = "first" +" "+ "last" 
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string 
decade = str(1990)
print(type(decade))
print(decade)

statement = "i like rock mucic from the " + decade + "s."
print(statement)

# Multiple linjes 
multiline = '''
hey, how are you? 

i was just checking in. 
                                  all good?
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nwhere\'s this at\\located?'
print(sentence)

# String Methods 

print("first")
print("first".lower())
print("first".upper())
print("first")

print(multiline.tittle())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                "
multiline = "                 " + "muliline" 
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.strip()))

# build a menu 
title = "menu".upper()
print("tittle".center(20, "="))
print("coffee".ljust(16, ".") + "$1".rjust(4))
print("muffin".ljust(16, ".")+ "$3".rjust(4))
print("chesscake".ljust(16, ".") + "$5".rjust(4))

print("")


# string index values 
print("frist"[1])
print("frist"[-1])
print("frist"[1:-1])
print("frist"[1:])

# some methods return boolean data
print("frist".startswith("D"))
print("frist".endswith("Z"))

# boolean data type 
myvalue = True 
x = bool("false")
print(type(x))
print(isinstance(myvalue, bool))

# Numerice data types

# integer type 
price = 100
best_price = int(80)
print(type("price")) 
print(isinstance(best_price, int))

 # float type 
gpa = 3.28
 Y = float(1.14)
 print(type(gpa))

 # complex type 
 comp_value = 5+3j
 print(comp_value.real)
 print(comp_value.imag)

# built-in functions for numbers 

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1 ))

import math 


print(math.pi)
print(math.spryt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number 
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attemt to cast incorrect data
#zip_value = int("New York")
