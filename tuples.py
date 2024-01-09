#Tuple: ordered, immutable, allows duplicate elements

mytuple = ("Max", 28, "Boston")
print(mytuple)

mytuple = "Max", 28, "Boston" #praantheses are optional

mytuple=("Max") #String
mytuple=("Max",) #Tuple
mytuple=tuple(["Max", 28, "Boston"]) #Tuple

item = mytuple[0] #Max
item = mytuple[-1] #Boston

# mytuple[0] = "Tim" #Error because tuple is immutable

#iterate
for i in mytuple:
  print(i)

if "Max" in mytuple:
  print("Yes")
else:
  print("No")


mytuple = ('a','p','p','l','e')
print(len(mytuple)) #5
print(mytuple.count('p')) #2
print(mytuple.count('o')) #0
print(mytuple.index('p')) #1
# print(mytuple.index('o')) #Error

#conversion between tuple and list
mylist = list(mytuple)
print(type(mylist))

mytuple = list(mylist)
print(type(mytuple))

#slicing
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5] #[start:stop]
print(b) #(3, 4, 5)

c = a[::2] #[start:stop:step]
print(c)

#unpacking
mytuple = ("Max", 28, "Boston")
name, age, city = mytuple
print(name) #Max
print(age) #28
print(city) #Boston

mytuple = (0, 1, 2, 3, 4)

i1, *i2, i3 = mytuple
print(i1) #0
print(i2) #[1, 2, 3] converted to list
print(i3) #4

# tuple more efficient than list since immutable so python can do more optimization internally
import sys
my_list = [0, 1, 2, 'hello', True]
my_tuple = (0, 1, 2, 'hello', True)
print(sys.getsizeof(my_list), 'bytes') # 96 bytes
print(sys.getsizeof(my_tuple), 'bytes') # 80 bytes

#also faster
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)) #0.045826180999999994
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)) #0.006678794000000002