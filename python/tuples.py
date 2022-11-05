# tuples are immutable

from itertools import zip_longest
from msilib.schema import Directory


t = ('a','b','c','d')

t1 = 'a',   # comma at the end is required to initialize the tuple with just a single character

t2 = tuple() # initialize an empty tuple


str = 'vishoiw'

zippedObject = zip(str,t) 


for pair in zippedObject:
    print(pair)

# Output of the above line
#    ('v', 'a')
#    ('i', 'b')
#    ('s', 'c')
#    ('h', 'd')
# note: t has 4 characters and str has 5 characters, when zipping /pairing `a` was ignored.. 
# both arguments needs to be of same length or argument with the shortest length becomes the size of the tuple.


listOfTuples = list(zippedObject) #

print(listOfTuples)

for index, element in enumerate(listOfTuples):    #another way to iterate the sequence/list 
    print(index,element)


# its common to have tuple as a key in the dictionary. 
#ex: firstname & lastname can be the key in the dictionary of telephone numbers

directory = dict()

directory[('firstname','lastname')] = '4169511222'

{('firstname','lastname'):'4169511222'}