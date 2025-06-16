''' list concatenation is the process of combining two or more lists into a single list.
'''
myFriends = ['Beril','Joshua','Ketty']
yourFriends = ['Alice', 'Stephen']

#make a new list using '+' operator, does not modify our original list
ourFriends = myFriends + yourFriends    # list concatenation
print(ourFriends)


#extend a list using extend() method,
#extend() modifies list1 in place and doesn't create a new list
myFriends.extend(yourFriends)
print(myFriends)


#Using the * Operator (Repetition and Concatenation)
list1 = [1, 2, 3]
list2 = ['Arif', 'Islam', 'Fakhrul']
list3 = ['Jan', 1, 'Feb', 2]
combineList = [*list1, *list2, *list3]     
print(combineList)
