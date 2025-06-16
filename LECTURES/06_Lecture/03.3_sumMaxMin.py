'''In Python, the built-in functions sum(), max(), and min() allow you to 
perform basic aggregate operations on lists. 

#sum(iterable, start)
#max(iterable, key)
#min(iterable, key)

sum()	Returns the sum of all numerical elements
max()	Returns the largest element in the list
min()	Returns the smallest element in the list

When applied to strings, max() returns the lexicographically largest string.
When applied to strings, min() returns the lexicographically smallest string.
If the list is empty, these functions raises a ValueError.
'''

#sum of a list
numbers = [1, 2, 3, 4, 5, 6]
total = sum(numbers)
print(total)

total2 = sum(numbers, 100)   #using the start parameter
print(total2)



#largest value of a list
largest = max(numbers)
print(largest)

# Using `max()` with strings
words = ["apple", "banana", "cherry"]
longest_word = max(words, key=len)
print(longest_word)  # Output: "banana"


#smallest value of a list
smallest = min(numbers)
print(smallest)

# Using `min()` with strings
words = ["apple", 'bpple',"banana", "cherry"]
shortest_word = min(words, key=len)
print(shortest_word)  # Output: "apple"



