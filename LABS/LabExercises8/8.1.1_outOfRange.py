def main() : 
    numbers = [10, 20, 30] 

    for i in range(len(numbers)) : 
        print(numbers[i+1])    # this index does not exist; will case an indexError 

if __name__ == "__main__" : 
    main()


'''Error Message in the console: 
IndexError: list index out of range '''