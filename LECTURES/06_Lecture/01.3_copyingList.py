'''When you want to create a copy of a list, that is a new list with the
same elements (in the same order) of the original one, you must
use the list() function'''

prices = [1, 3, 4.3, 6, 7.5]
values = list(prices)
print(values)

prices[0] = 100 
print(values)
print(prices)

last = prices[-1]
last = prices[len(prices)-1]
print("The last value of the prices list is:", last)