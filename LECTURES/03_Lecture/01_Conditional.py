#this program simulates an elabator panel that skips 13th floor

floor = int(input("Insert floor number: "))

if floor > 13:
    actualFloor = floor - 1
    print("The elevator will travel to the actual floor: ",actualFloor)
    
elif floor == 13:
    print("There is no 13th floor")
    
else:
    actualFloor = floor
    print("The elevator will travel to the actual floor: ",actualFloor)

