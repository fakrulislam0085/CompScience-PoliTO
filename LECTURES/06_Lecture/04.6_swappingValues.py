#swapping two values
numberList = [32, 29, 67.5, 64, 34.5]

temp = numberList[2]
numberList[2] = numberList[4]
numberList[4] = temp
print(numberList)


#exercise - p6.30
a =[1, 4, 9, 16]
b =[9, 7, 4, 9, 11, 2]

min_length = min(len(a), len(b))
alternated_list = []

for i in range(min_length) :
    alternated_list.append(a[i])
    alternated_list.append(b[i])

#append the remaining elements from the list
if len(a) > min_length :
    alternated_list.extend(a[min_length:])
elif len(b) > min_length :
    alternated_list.extend(b[min_length:])

print("Alternated List:", alternated_list)