'''When you copy a list variable into another, both variables refer to the same list,
this is called list Aliases''' 
scores = [10, 20, 30, 40, 50]
values = scores 

print(values)
scores[2] = 300     #You can modify the list through either of the variables
print(values[2])    # we modified scores[2]; but our values[2] will be also modified
print(values)
print(scores)

two_from_last = scores[-2]      # In case of reversing, index starts from 1 
print("The second value form last in the scores list is:", two_from_last)




