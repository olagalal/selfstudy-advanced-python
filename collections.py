#collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter
a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter) #Counter({'a': 5, 'b': 4, 'c': 3})
print(my_counter.keys()) #dict_keys(['a', 'b', 'c'])
print(my_counter.most_common(2)) #[('a', 5), ('b', 4)]
print(my_counter.most_common(1)[0][0]) #a
print(list(my_counter.elements())) #then you can iterate over this list

from collections import namedtuple
Point = namedtuple('Point', 'x,y') #this will create a class Point with 2 fields x and y
pt = Point(1,-4)
print(pt)
print(pt.x, pt.y)

from collections import OrderedDict 
#it's not important any more (py 3.7) 
#it's a regular dict that remember the order in which a value was entered
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict) 

from collections import defaultdict
#It's a subclass of dict that calls a factory function to supply missing values in a dictionary whose key hasn't been set
d = defaultdict(int) #you can try float or list or ..
d['a'] = 1
d['b'] = 2
print(d)
print(d['a'])
print(d['c']) #return defalt value of int which is 0

from collections import deque
#deque is a double-ended queue, which is a generalization of stacks and queues. 
#It has append() and pop() operations in O(1) time.
d = deque()
d.append(1)
d.append(2)
print(d)

d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

# d.clear() #remove all elements

# d.extend([4, 5, 6])
# print(d)

d.extendleft([4, 5, 6])
print(d)

d.rotate(1) #shift right by 1
print(d)

d.rotate(-2) #shift left by 2
print(d)
