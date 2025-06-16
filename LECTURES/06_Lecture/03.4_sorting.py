#sorted() function
numbers = [5, 2, 6, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [2, 5, 5, 6]
sortedNum = sorted(numbers, reverse = True)  #reverse
print(sortedNum)


#list.sort() method
'''Sorts the list in place.
Modifies the original list.
Syntax: list.sort(key=None, reverse=False)
key: A function that serves as a key for the sort comparison.'''
numbers = [5, 2, 6, 5, 7, 8]
numbers.sort()
print(numbers)  # Output: [2, 5, 5, 6, 7, 8]
numbers.sort(reverse = True)    #reverse
print(numbers)


#sorting with custom keys
words = ["banana", "pie", "apple"]
words.sort(key=len)
print(words)
