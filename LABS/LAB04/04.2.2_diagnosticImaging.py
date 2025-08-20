import math 

HALF_LIFE = 6   # It has a half-life of 6 hours
A0 = float(input("Enter the initial amount to Technetium-99: "))
LAMBDA = math.log(2) / HALF_LIFE    # Decay rate 

def main() : 
    for time_hour in range(0, 25) :     # Total 24 hours in a day
        A = A0 * math.exp(-LAMBDA * time_hour) 
        print(f"Relative quantity remaining after the {time_hour} hour: {A/A0}")

if __name__ == "__main__" : 
    main() 