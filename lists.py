mylist = ["banana", "cherry", "apple"]
print(mylist)

item = mylist[0]
print(item)

item = mylist[-1]
print(item)

#to print the whole list
for i in mylist:
  print(i)

# mylist2 = [5, True, 'apple', 'apple']
  
if 'banana' in mylist:
  print("YES")
else:
  print("NO")

if 'lemon' in mylist:
  print("YES")
else:
  print("NO")

#useful methods
print(len(mylist))
mylist.append('lemon')
print(mylist)

mylist.insert(1, 'blueberry')
print(mylist)

item = mylist.pop() #return the last item and then remove it 
print(item)
print(mylist)

mylist.remove('apple')
print(mylist)

# mylist.clear() #to remove all elements

mylist.reverse()
print(mylist)

# mylist.sort()
# print(mylist)

#to create new list that is sorted without manipulating the original 
new_list = sorted(mylist)
print(mylist)
print(new_list)

#create list with five zeros 
mylist = [0] * 5
print(mylist) #[0, 0, 0, 0, 0]

#concat lists (using + opertator)
mylist2 = [1, 2, 3, 4, 5]
new_list = mylist + mylist2
print(new_list)

#slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
print(a)

b = mylist[:5]
print(b)

c = mylist[1:]
print(c)

d = mylist[::2] #step = 2
print(d)

e = mylist[::-1] #nice trick to reverse the list

#copying
list_org = ['banana', 'cherry', 'apple']
list_cpy = list_org
list_cpy.append('lemon') #this will affect both lists (refrence)
print(list_org)
print(list_cpy)

#actual copy
list_org = ['banana', 'cherry', 'apple']
list_cpy = list_org.copy()
# list_cpy = list(list_org) #another option
# list_cpy = list_org[:] #third option
list_cpy.append('lemon') #this will affect both lists (refrence)
print(list_org)
print(list_cpy)

#list comprehension
mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist] #expression + for loop

print(mylist)
print(b)