values = [1, 3, 5, 6, 12, -3, 6, 0, -30]
largest = values[0]

for i in range(1, len(values)) :
    if values[i] > largest :
        largest = values[i]
print("Largest: ", largest)


smallest = values[0]
for i in range(1, len(values)) :
    if values[i] < smallest :
        smallest = values[i]
print("Smallest: ", smallest)



#string
names = ['Ann', 'Charlotte', 'Zachary', 'Bill']
longestName = max(names)
print(longestName)

longestN = names[0]
for i in range(1, len(names)) :
    if len(longestN) < len(names[i]) :
        longestN = names[i]
print(longestN)

