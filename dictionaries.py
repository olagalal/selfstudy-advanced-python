# Dictionary: key-value pairs, unordered, mutable

mydict = {"name":"Max", "age":28, "city":"New York"}
print(mydict)

mydict = dict(name="Mary", age=27, city="Boston")
print(mydict)

#get value of the key
value = mydict["name"]
print(value)

# value = mydict["lastname"] #Error

#adds new key:value pair
mydict["email"] = "me@xyz.com"
print(mydict)

#overwrites value of "email"
mydict["email"] = "max@xyz.com"
print(mydict)

#delete item
del mydict["name"]
print(mydict)

#pop(arg)
mydict.pop("age")
print(mydict)

#popitem() removes last element in dictionary
mydict.popitem()
print(mydict)

mydict = {"name":"Max", "age":28, "city":"New York"}

if "name" in mydict:
  print(mydict["name"])

try:
  print(mydict["lastname"])
except:
  print("error")

#loop
# for i in mydict: #or
for i in mydict.keys():
  print(i)

for i in mydict.values():
  print(i)

for key, value in mydict.items():
  print(key, value)

#copy dictionary
mydict_cpy = mydict
print(mydict_cpy) #{'name': 'Max', 'age': 28, 'city': 'New York'}

mydict_cpy["email"] = 'max@xyz.com' #both will be modified
print(mydict) #{'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@xyz.com'}
print(mydict_cpy) #{'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@xyz.com'}

mydict = {"name":"Max", "age":28, "city":"New York"}
mydict_cpy = mydict.copy()
mydict_cpy["email"] = 'max@xyz.com' #both will be modified
print(mydict) #{'name': 'Max', 'age': 28, 'city': 'New York'}
print(mydict_cpy) #{'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@xyz.com'}

#another syntax to copy
mydict_cpy = dict(mydict)

#update() to merge dicts
mydict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
mydict_2 = dict(name="Mary", age=27, city="Boston")
mydict.update(mydict_2)
print(mydict) #{'name': 'Mary', 'age': 27, 'email': 'max@xyz.com', 'city': 'Boston'}

#numbers can be used as a key
mydict = {3:9, 6:36, 9:81} #possible 
value = mydict[3] #9

#tuples can be used as a key
mytuple = (8,7)
mydict = {mytuple: 15}
print(mydict) #{(8, 7): 15}

#lists can't (because it's mutable and unhashable)
# mylist = [8,7]
# mydict = {mylist: 15} #Error