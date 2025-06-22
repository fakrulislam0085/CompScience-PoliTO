#set operations at a glance

'''
#Create a new set that is either empty or a duplicate copy of sequence seq
or that contains the initial elements provided.
s = set() 
s = set(seq)
s = {'a', 'b', 'c'}

#return a shallow copy of the set
s.copy()

#return the number of elements in set s (cardinality of s)
len(s)



#determine if element is in the set or not
if element in s
if element not in s 

#add element to the set
s.add(element)

#remove element from the set
s.remove(element)
s.discard(element)

#remove and return an arbitrary element from the set
s.pop()

#remove all elements from the set
s.clear()



#return a boolean indicating whether set s is a subset of t 
s.issubset(t)

#return a boolean indicating whether set s is a proper subset of t
s.issuperset(t)

#return a boolean indicating whether set s and set t are equal
s == t
s != t



#union and intersection of two sets
s.union(t)
s.intersection(t)

#difference of two sets
s.difference(t)



###Set operations using short operators
x1.union(x2)                x1 || x2
x1.intersection(x2)         x1 && x2
x1.difference(x2)           x1 - x2
x1.symmetric_difference(x2) x1 ^ x2
x1.issubset(x2)             x1 <= x2
                            x1 < x2
x1.issuperset(x2)           x1 >= x2
                            x1 > x2

'''