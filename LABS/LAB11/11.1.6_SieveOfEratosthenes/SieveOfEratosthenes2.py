# Solution 2
from math import * 

def main() : 
    n = int(input("Enter the input: ")) 

    numberSet = set(x for x in range(2, n+1))
    print(numberSet) 

    to_remove = set()
    for value in numberSet : 
        for i in range(2, floor(sqrt(n)+2), 1) : 
            a = value * i 
            to_remove.add(a)         # or numberSet.discard(a) 

    numberSet -= to_remove 
    print(numberSet)
    
if __name__ == "__main__" : 
    main() 
