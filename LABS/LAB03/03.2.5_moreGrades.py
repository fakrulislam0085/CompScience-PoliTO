# Adding "+" and "-". If the grades is greater than the integer value for more than 0.15, 
# then it will be closer to 0.3 than to 0.0 so it "deservs" a "+". Similarly for the "-".
''' 
A+ = 4.0
A = 4.0 
B = 3.0 
C = 2.0 
D = 1.0 
F = 0.0 

2.85 = B
2.80 = B- 
'''
def convert_to_letter_grade(num_grade) : 

    if 3.85 <= num_grade <= 4.0 : 
        return 'A' 
    elif 3.50 <= num_grade < 3.85 : 
        return 'A-' 
    elif 3.15 <= num_grade < 3.50 :
        return 'B+'
    elif 2.85 <= num_grade < 3.15 :
        return 'B' 
    elif 2.50 <= num_grade < 2.85 : 
        return 'B-' 
    elif 2.15 <= num_grade < 2.50 :
        return 'C+' 
    elif 1.85 <= num_grade < 2.15 : 
        return 'C' 
    elif 1.50 <= num_grade < 1.85 :
        return 'C-'
    elif 1.15 <= num_grade < 1.50 : 
        return 'D+' 
    elif 0.85 <= num_grade < 1.15 :
        return 'D'
    elif 0.50 <= num_grade < 0.85 :
        return 'D-' 
    else : 
        return 'F'
    

def main():
    num_grade = float(input("Enter the Number Grade: ")) 

    # Input validation 
    if num_grade < 0.0 or num_grade > 4.0 :
        print("Wrong Input. Please Run the code again and choose a grade between 0.0~4.0")

    letter_grade = convert_to_letter_grade(num_grade)
    print(f"The corresponding letter grade of {num_grade} is: {letter_grade}")

if __name__ == "__main__":
    main()



