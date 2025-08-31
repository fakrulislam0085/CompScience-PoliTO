def leapYearTrack(y) : 
    if y%4 != 0 or (y%100 == 0 and y%400 != 0) : 
        print(f"{y} is not a leap year.")
    else :
        print(f"{y} is a leap year.") 
    

def main() : 
    year = int(input("Enter the Year(greater than 1582): ")) 
    leapYearTrack(year) 

if __name__ == "__main__" : 
    main() 