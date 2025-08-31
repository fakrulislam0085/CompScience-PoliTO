def seasonTracker(d, m) : 
    if m in (1, 2, 3) :     # Tuple
        season = "WINTER"   
    elif m in (4, 5, 6) : 
        season = "SPRING" 
    elif m in (7, 8, 9) :  
        season = "SUMMER" 
    elif m in (10, 11, 12) : 
        season = "FALL" 
    
    if m%3 == 0 and d>=21 : 
        if season == "WINTER" : 
            season = "SPRING" 
        elif season == "SPRING" : 
            season = "SUMMER" 
        elif season == "SUMMER" : 
            season = "FALL" 
        else : 
            season = "WINTER"

    print(f"The {d} number day of {m} number month is on {season} season!")    

def main() : 
    day = int(input("Enter the day number(INTEGER): ")) 
    month = int(input("Enter the month number(INTEGER): ")) 

    seasonTracker(day, month) 

if __name__ == "__main__" : 
    main() 