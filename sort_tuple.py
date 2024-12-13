#Sort a tuple of tuples by 2nd item
from  operator import itemgetter

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

#Use the itemgetter() function from the operator module together with the sorted() function,this will sort the tupple by the second element
print(tuple(sorted(tuple1, key = itemgetter(1))))