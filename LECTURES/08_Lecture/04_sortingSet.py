'''Use the sorted() function, which returns a list (not a set) of the
elements in sorted order.
* Numbers: increasing order (by default, or decreasing with reverse=True)
* Strings: lexicographical order
'''

numberSet = {1, 2, 4, 6, 8, 0 }
sorted_numberSet = sorted(numberSet)
print(sorted_numberSet) 

stringSet = {'Ami', 'jami', 'gemini', 'banana'}
sorted_stringSet = sorted(stringSet)
print(sorted_stringSet)


