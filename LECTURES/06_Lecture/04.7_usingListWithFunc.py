#using list in a function
def sumsq(values) :
    total = 0
    for element in values :
        total = total + element ** 2 
    return total
 
def main() :
    values = [10, 20, 30, 40, 50]
    result = sumsq(values)
    print(result)

main()



#modifying list elements in function 
def multiply(values, factor) :
    for i in range (len(values)):
        values[i] = values[i] * factor 
    return values

def main() :
    values = [1, 2, 3, 4, 5, 6, 7]
    factor = 2 
    newValues = multiply(values, factor)
    print(newValues)

main()



#example- page 75
def printReverse(values) :
    reverseValues = values[ :: -1]
    print(reverseValues)

def multiply(values, x) :
    for i in range(len(values)) : 
        values[i] = values[i] * x
    printReverse(values)

def readFloats() :
    values = list(map(int, input("Read the values from the user: ").split()))
    return values
    
def main() :
    values = readFloats()
    x = 10
    multiply(values, x)

main() 
