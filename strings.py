#String: ordered, immutable, text representation

my_string = "Hello World"
my_string = 'I\'m a progammer'

#use """ for multiline strings
#use \ to remove line
multilines = """
this is \
a multiline
string
"""

print(my_string)
print(multilines)

my_string = "Hello World"
#get first character from my_string (it's like a list of chars)
char = my_string[0] #H
print(char)

#get last character from my_string
char = my_string[-1] #d
print(char)

#we can't change chars
#my_string[0] = 'h' #Error

#slice
substring = my_string[:5]
print(substring)

#reverse string
reverseString = my_string[::-1]
print(reverseString)

#concatenate strings
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

#print every letter in greeting
for i in greeting:
  print(i)

#find 'ello' within greeting
if 'ello' in greeting:
  print("yes")
else:
  print("no")

#methods 
#strip() removes white spaces
my_string = "   Hello World   "
my_string = my_string.strip() #doesn't change string in place
print(my_string)

#upper() sets string as uppercase
print(my_string.upper())

#lower() sets string as lowercase
print(my_string.lower())

#startswith(arg1) returns True if string starts with the arg
print(my_string.startswith("He")) #True

#endwith(arg1) returns True if string ends with the arg
print(my_string.endswith("World")) #True

#find(arg1) returns index of the first match
print(my_string.find("o")) #4

#count(arg1) returns number of matches with the arg
print(my_string.count("o")) #2

#replace(arg1, arg2) replaces arg1 with arg2
print(my_string.replace("World", "Abe")) #Hello Abe

#split(arg1) splits apart a string into a list, delimiter is a space by default
my_string = "How are you doing"
my_list = my_string.split(" ")
print(my_list)

#join(arg1) converts list into a string
newString = " ".join(my_list)
print(newString)

#converting list into a string: join vs loop
from timeit import default_timer as timer
my_list = ["a"] * 10
# my_list = ["a"] * 1000000

#using loop (bad)
start = timer()
my_string = ''
for i in my_list:
  my_string += i #very expensive operation
stop = timer()
print(stop-start)

#using join (good)
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop-start)

#formatting strings
#% deprecated
var = "Tom"
my_string = "The variable is %s" %var
print(my_string)
#%s for strings
#%d for decimal
#%f for float (by default it has 6 digits after the point)

#format() deprecated
my_string = "The variable is {}".format(var)
print(my_string)

var = 3.1234567
var2 = 3.16093232
my_string = "The variable is {:.2f} and {:4f}".format(var, var2)
print(my_string)

#f-string (py 3.6)
my_string = f"The variable is {var*2} and {var2}" #we can perform operations
print(my_string)