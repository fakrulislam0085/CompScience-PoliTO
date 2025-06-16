#list of days name
day_name = ['sat', 'sun', 'mon', 'wed', 'thur', 'fri']
day_name[3] = 'Tue'
print(day_name)
print()

#without index
for element in day_name :
    print(element, end=" ")
print("\n")

#with index 
for i in range(len(day_name)):
    print(i, day_name[i])
print()

#or - using enumerate function
for indx, element in enumerate(day_name) :
    print(indx, "-", element)
