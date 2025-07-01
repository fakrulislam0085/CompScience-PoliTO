import random 

def operationOnList(randomList) :
    evenIndexElement = []
    evenValue = []
    reverseList = randomList[::-1] 
    first_element = randomList[0] 
    last_element = randomList[-1] 

    for i, num in enumerate(randomList) :
        if i%2 == 0 :
            evenIndexElement.append(randomList[i]) 
        if num % 2 == 0 :
            evenValue.append(num) 

    print(f"I. The even Index values from our list: {evenIndexElement}")
    print(f"II. The even values from our list: {evenValue}")
    print(f"III. The reverse list of our random List(1 to 100): {reverseList}")
    print(f"IV. The first element of our random list(1 to 100): {first_element} ")
    print(f"IV. The last element of our random List(1 to 100): {last_element}")

def randomNumList() :
    count = 1
    randomList = [] 
    
    while count < 11 :
        choice_a_Num = random.randint(1, 100) 
        randomList.append(choice_a_Num)
        count += 1 
    
    operationOnList(randomList)

def main() :
    randomNumList()

if __name__ == "__main__" : 
    main()
