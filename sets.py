#Set: unordered, mutable, unique
myset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10}
print(myset)

myset = set([2, 4, 6, 8, 10])
print(myset)

myset = set("Hello") #get unique chars

#empty set
myset = {} #this is dict
myset = set() #this is set

#add elements
myset.add(2)
myset.add(4)
myset.add(6)

print(myset)

#remove elements
myset.remove(6)
# myset.remove(0) # will raise an error

myset.discard(0) #will not raise an error
myset.discard(2)

#to empty a set
myset.clear()

# print(myset.pop()) #it will remove arbitrary elements and return it

for i in myset:
  print(i)

if 1 in myset:
  print("YES")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

#union() combines 2 sets without dupes
u = odds.union(evens)
print(u)

#intersection() returns dupes within 2 sets
i = odds.intersection(primes)
print(i) #{3, 5, 7}

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

#difference() returns the difference in 2 sets
diff = setA.difference(setB)
print(diff)  #{4, 5, 6, 7, 8, 9}
diff = setB.difference(setA)
print(diff)  #{10, 11, 12}

#symmetric_difference() returns the unique elements in 2 sets
diff = setB.symmetric_difference(setA)
print(diff) #{4, 5, 6, 7, 8, 9, 10, 11, 12}

#update() combines unique elements within 2 sets
setA.update(setB) #modify in place
print(setA)

#intersection_update() returns a set of common elements
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.intersection_update(setB)
print(setA) #{1, 2, 3}

#difference_update() removes commons elements on setA only
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.difference_update(setB)
print(setA) #{4, 5, 6, 7, 8, 9} #removed {1, 2, 3} that were found on setB

#symmetric_difference_update() filters out the common elements from 2 sets, returns the 2 sets combined
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.symmetric_difference_update(setB)
print(setA) #{4, 5, 6, 7, 8, 9, 10, 11, 12}

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

#issubset() checks if a set matches completely with the argument set
print(setA.issubset(setB)) #False
print(setB.issubset(setA)) #True

#issuperset() checks if an argument set matches completely with a set
print(setA.issuperset(setB)) #True

#isdisjoint() returns true if 2 sets are unique
print(setA.isdisjoint(setB)) #False

#copy() copies a set into another
setB = setA.copy()
setB = set(setA)

#frozenset() is an immutable set
a = frozenset([1, 2, 3, 4])
print(a)
