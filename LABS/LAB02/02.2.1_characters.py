def main() : 
    word = input("Enter the string: ") 

    if(len(word) >= 6) :
        newWord = word[:3] + "..." + word[-3:]
        print(f"New String is: {newWord}")

    elif len(word) < 6 and len(word) >= 3 : 
        print(f"New String is: {word[:3]}...{word[-3:]}")
    else :      # Less than 3 characters 
        print(f"New String is: {word[:3]}...{word[-3:]}")
        
if __name__ == "__main__": 
    main()
