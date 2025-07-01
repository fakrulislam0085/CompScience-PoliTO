def sum_without_smallest(v) :
    findOutMin = min(v)     #returns the min() value from the list v 
    result = 0 
    for value in v :
        if value != findOutMin :
            result += value 
    return result


myList = list(map(int, input("Enter the list values: ").split()))
Total_sum = sum_without_smallest(myList)
print(f"Sum of the list without the minimum value: {Total_sum}")