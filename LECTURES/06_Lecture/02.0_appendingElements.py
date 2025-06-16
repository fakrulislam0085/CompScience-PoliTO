#1
friends = []

#2
friends.append('Harry')

#3 
friends.append('Momota')
friends.append('Harita')
friends.append('Komola')

print(friends)      #flat printing


print()
for indx, element in enumerate(friends) :   #using for loop to print
    print(indx, "-", element)


print()
for i in range(len(friends)) :      #using range function
    print(i, friends[i])


print()
for element in friends :
    print(element)