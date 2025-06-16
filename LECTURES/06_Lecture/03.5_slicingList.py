#Create a temperature list
temperatures = [18, 21, 24, 33, 39, 36, 30, 22, 18]

#normal slicing
thirdQuarter = temperatures [6:9]
print(thirdQuarter)


# x includes all elements up to, but not including, position 4
x = temperatures[:4]
print(x)


# includes all elements starting at position 4 to the end of the list
y = temperatures[4:]
print(y)



# all elements from start to end. Equivalent to making a copy like x = list(temperatures)
z = temperatures[ : ]
print(z)


#A third index can be used to specify the step (implicitly = 1)
#All elements with even indices
list1 = temperatures[::2]
print(list1)


#The entire list, but in reverse order
reverseList = temperatures[:: -1]
print(reverseList)



#With lists, we can use slicing for assignments too
#replaces the values in index 6 and 7
temperatures[6:8] = [66, 77]
print(temperatures)

#if the length of the replacement is different from the length 
#-of the slice, elements will be removed or added to the list
temperatures[4:5] = [100, 200, 300]
print(temperatures)