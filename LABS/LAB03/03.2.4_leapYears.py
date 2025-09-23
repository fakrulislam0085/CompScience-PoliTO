# Check whether a given year is a leap year according to the Gregorian rules.
# Rule summary (valid from 1582 onward):
#  - Years divisible by 4 are leap years,
#  - except years divisible by 100, which are NOT leap years,
#  - except years divisible by 400, which ARE leap years.
# Example: 1900 -> not leap (divisible by 100 but not 400); 2000 -> leap.

def leapYearTrack(y) : 
    # If the year is NOT divisible by 4, or it is a century year not divisible by 400,
    # then it is NOT a leap year. Otherwise, it is a leap year.
    if y%4 != 0 or (y%100 == 0 and y%400 != 0) : 
        print(f"{y} is not a leap year.")
    else :
        print(f"{y} is a leap year.") 
    
def main() : 
    year = int(input("Enter the Year(greater than 1582): ")) 
    leapYearTrack(year) 

if __name__ == "__main__" : 
    main() 
