'''You can use the == operator to compare whether two lists have
the same elements, in the same order
'''

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]

print(list1 == list2)  # Output: True (same elements, same order)
print(list1 == list3)  # Output: False (same elements, different order)
print(list1 != list3)  # Output: True (they are different)