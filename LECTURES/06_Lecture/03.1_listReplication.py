''' List replication is the process of creating multiple copies of a list's elements in Python. 
This is typically done using the * (multiplication) operator

▪ The integer specifies how many copies of the list should be concatenated
▪ One common use of replication is to initialize a list with a fixed value

#replicated_list = original_list * n

'''
#simple list replication
monthInQuarter = [1, 2, 3, 4]
replicatedList = monthInQuarter * 3  
print(replicatedList)

#a list with 12 zeroes 
monthlyScores = [0] * 12 
print(monthlyScores)



#replication of string in a list
words = ["hello", "world"]
replicated = words * 2
print(replicated)  # Output: ['hello', 'world', 'hello', 'world']


#replication of nested list 
nestedList = [[1, 3]]
replicateNesLis = nestedList * 3 
print(replicateNesLis)
# Modifying one element affects all copies
nestedList[0][0] = 99
print(replicateNesLis)  # Output: [[99, 2], [99, 2], [99, 2]]