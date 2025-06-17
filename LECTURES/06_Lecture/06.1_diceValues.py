#Our task is to analyze whether a dice is fair by counting how often each value (1, 2, 3, 4, 5, 6) appears
'''Our input will be a series of dice toss values
* For example, if the values are: 1, 2, 1, 3, 4, 6, 5, 6
* The result is 1: 2; 2: 1; 3: 1; 4: 1; 5: 1; 6: 2'''

def count_inputs(s) :
    """Count how often each value appears in the dice tosses."""
    #initialize counters for each side of the dice
    counters = [0] * s

    print("Enter dice toss values(enter 0 to finish): ")
    while True :
        value = int(input())
        if value == 0 :
            break
        if 1 <= value <= s :
            counters[value-1] += 1
        else :
            print(f"Value {value} is out of range. Please enter a number between 1 and {s}.")
    
    return counters

# def print_counters(c) :
#     """Print the counters in a formatted way."""
#     for indx, count in enumerate(c, start = 1) :
#         print(f"{indx} : {count}")

#printing as a histogram
def print_counters(c) :
    total = sum(c) 
    for indx, count in enumerate(c, start=0) :
        percentage = (count / total) * 100
        bar = '+' * int(percentage)
        print(f"{indx+1} : ({percentage:.1f}) {bar}")

def main() :
    """Main function to analyze dice fairness."""
    sides = 6 
    counters = count_inputs(sides)
    print_counters(counters)

main()