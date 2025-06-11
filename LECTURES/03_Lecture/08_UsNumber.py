number = input("Take the number input: ")

if (len(number) == 13 
    and number[0] == '(' 
    and number[4] == ')' 
    and number[8] == '-' 
    and number[1:4].isdigit() 
    and number[5:8].isdigit() 
    and number[9:13].isdigit()):
    print("This is a US cellphone number")
else:
    print("This is not a US number")