# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))  #[(1, 3), (1, 4), (2, 3), (2, 4)]

a = [1,2]
b = [3]
prod = product(a,b)
prod = product(a,b, repeat = 2) #[(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]
print(list(prod))


from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm)) #[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

perm = permutations(a, 2) #with len=2
print(list(perm)) #[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


from itertools import combinations
a = [1, 2, 3, 4]
comb = combinations(a, 2) #len here is mandatory 
print(list(comb)) #[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


from itertools import combinations_with_replacement
comb = combinations_with_replacement(a, 2) #len here is mandatory
print(list(comb)) #[(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]


from itertools import accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc)) #[1, 3, 6, 10]

import operator
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc)) #[1, 2, 6, 24]

a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(a)
print(list(acc)) #[1, 2, 5, 5, 5]


from itertools import groupby

def smaller_than_3(x):
  return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
print(group_obj)
for key, val in group_obj:
  print(key, list(val)) 
#True [1, 2]
#False [3, 4]
  
#using lambda
a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x < 3)
for key, val in group_obj:
  print(key, list(val)) 
#True [1, 2]
#False [3, 4]

persons = [
    {'name': 'Tim', 'age': 25},
    {'name': 'Dan', 'age': 25},
    {'name': 'Lisa', 'age': 27},
    {'name': 'Claire', 'age': 28},
]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, val in group_obj:
  print(key, list(val)) 
#25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
#27 [{'name': 'Lisa', 'age': 27}]
#28 [{'name': 'Claire', 'age': 28}]

from itertools import count, cycle, repeat

#count(start=0, step=1) returns an iterator that counts its starting value, and increments by step, each time it is iterated
for i in count(10):
  print(i)
  if i == 15:
    break

#cycle iterates through an iterable, indefinitely
a = [1, 2, 3]
for i in cycle(a):
  print(i)
  if i == 2:
    break

#repeat
for i in repeat(1, 4):
  print(i)
