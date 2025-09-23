# This program shifts all elements one position to the right, with the last element 
# moving to the first position.The program prints the list after each shift operation

def shiftList(myList) :
    last_element = myList[-1]
    for i in range(len(myList)-1, 0, -1) :
        myList[i] = myList[i-1]

    myList[0] = last_element
    return myList

def main() :
    myList = list(map(int, input("Enter the values: ").split()))
    for _ in range(len(myList)):
        print(f"The shifted values of the list is:{shiftList(myList)}")

if __name__ == "__main__" :
    main()


