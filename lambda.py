# lambda arguments: expression
add10 = lambda x: x + 10 #this is a function
print(add10(5)) #15

#it's like this 
def add10_func(x):
  return x + 10

#lambda functions can have multiple args
mult = lambda x, y: x*y
print(mult(2, 7)) #14

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D) #sort our list by the first val in the tuple
print(points2D)
print(points2D_sorted) #[(1, 2), (5, -1), (10, 4), (15, 1)]

points2D_sorted = sorted(points2D, key=lambda x: x[1]) #sort our list by the second val in the tuple
print(points2D_sorted) #[(5, -1), (15, 1), (1, 2), (10, 4)]
#similar to:
# def sort_by_y(x):
#   return x[1]

#let's sort them by the sum of each 
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1]) #sort our list by the second val in the tuple
print(points2D_sorted) #[(1, 2), (5, -1), (10, 4), (15, 1)]

#let's use lambda with map, filter, and reduce
#map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(b) #map obj
print(list(b)) #[2, 4, 6, 8, 10]

#another way to achive this using list comprehension
c = [x*2 for x in a]
print(c) #[2, 4, 6, 8, 10]

#filter(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2==0, a)
print(list(b)) #[2, 4, 6]

#another way to achive this using list comprehension
c = [x for x in a if x%2==0]
print(c) #[2, 4, 6]

#reduce(func, seq)
from functools import reduce
#to apply a particular function passed in its argument to all of the list elementsto apply a particular function passed in its argument to all of the list elements
a = [1, 2, 3, 4, 5, 6]

product_a = reduce(lambda x, y: x*y, a)
print(product_a) #720
