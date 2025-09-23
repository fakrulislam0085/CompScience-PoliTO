def remove_min(myList) :
    min_val = myList[0]    # Suppose the first value of  myList is minimum 
    withoutMin = []

    # Find out the minimum value 
    for value in myList :
        if value < min_val :
            min_val = value 
    
    # Create a list without minimum value 
    for value in myList :
        if value != min_val :
            withoutMin.append(value)

    return withoutMin

def main() :
    mylist = list(map(int, input("Enter the values of the list: ").split()))
    withoutMin = remove_min(mylist)
    print(f"Now our new List is: {withoutMin}")

if __name__ == "__main__" : 
    main()