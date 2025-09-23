import random 

# Generates a list of 20 random integers (0-99) and prints it sorted.
def orderedList(integerList) :
    #sortedList = sorted(integerList)
    
    print(f"The generated list: {integerList}")
    integerList.sort()
    print(f"The sorted list: {integerList}")

def creating_random_list() :
    integerList = []

    for i in range(0, 20) :
        generatedNum = random.randint(0, 99) 
        integerList.append(generatedNum)

    orderedList(integerList)    

def main() :
    creating_random_list()

if __name__ == "__main__" : 
    main() 