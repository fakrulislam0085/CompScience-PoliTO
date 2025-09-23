def alternating_Sum():
    # To remove any leading or trailing spaces from the input we use .strip()
    line = input("Enter numbers separated by spaces (terminate by pressing Enter on a blank line): ").strip()
    
    # Split the line into a list of integers
    number_list = list(map(int, line.split()))
    alternating_sum = 0
    
    # Calculate the alternating sum
    for i, num in enumerate(number_list):
        if i % 2 == 0:
            alternating_sum += num
        else:
            alternating_sum -= num
    
    return alternating_sum

print(f"The alternating sum is: {alternating_Sum()}")
