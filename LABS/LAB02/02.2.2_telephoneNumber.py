def main() : 
    phoneNum = input("Enter the 10-digit telephone number: ") 

    formattedNum = '(' + phoneNum[:3] + ')' + ' ' + phoneNum[3:6] + '-' + phoneNum[6:]
    print(f"Telephone Number formatted in the U.S. style: {formattedNum}")

if __name__ == "__main__" : 
    main() 