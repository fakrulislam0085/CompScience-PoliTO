def processTheList(ourList) :
    n = len(ourList)

    if n == 1 :
        return 
    
    #update the first value 
    ourList[0] = (ourList[0] + ourList[1]) / 2 
    
    #update the middle values 
    for i in range(1, n-1) :
        ourList[i] = (ourList[i-1] + ourList[i] + ourList[i+1]) / 3
    
    #update the last element 
    ourList[n-1] = (ourList[n-2] + ourList[n-1]) / 2

    return ourList

def main() :
    ourList = list(map(int, input("Enter the values: ").split()))
    ourList = processTheList(ourList)

    #format each value to two decimal places 
    formatted_list = [f"{x:.2f}" for x in ourList] 
    print(f"Without noise, the measurement list is: {' '.join(formatted_list)}")

if __name__ == "__main__" : 
    main()