def main() : 
    letterGrade = input("Enter a lette grade: ").upper() 

    if letterGrade[0] == 'A' : 
        num = 4.0 
    elif letterGrade[0] == 'B' : 
        num = 3.0 
    elif letterGrade[0] == 'C' : 
        num = 2.0 
    elif letterGrade[0] == 'D' : 
        num = 1.0 
    else :
        num = 0.0 

    # Now let's work on the +/- sign 
    if len(letterGrade) > 1 and letterGrade[0] != 'F' : 
        if letterGrade[1] == '+' and letterGrade[0] != 'A' : 
            num = num + 0.3
        elif letterGrade[1] == '-' :
            num = num - 0.3 
    
    print(f"The corresponding numerical grade of {letterGrade} is: {num}")
    
if __name__ == "__main__" : 
    main() 