import random 

def find_longest_sequence(dice_rolls) :
    max_length = 1 
    current_length = 1 
    start_indx = 0 
    longest_start = 0

    for i in range(1, len(dice_rolls)) :
        if dice_rolls[i] == dice_rolls[i-1] :
            current_length += 1 
        else :
            if current_length > max_length :
                max_length = current_length 
                longest_start = start_indx 
            current_length = 1 
            start_indx = i 
    # Final check in case the longest sequence is at the end of the list 
    if current_length > max_length :
        max_length = current_length 
        longest_start = start_indx

    return longest_start, max_length

def format_with_parentheses(dice_rolls, start, length) :
    result = []     # A list of string to hold the elements from dice_rolls and char '(' and ')'

    for i in range(len(dice_rolls)) :
        if i == start :
            result.append('(')

        result.append(str(dice_rolls[i]))

        if i == start + length -1 :
            result.append(')')

    return ' '.join(result)

def main() :
    # A standard die has 6 sides, numbered 1 to 6.
    dice_rolls = [random.randint(1, 6) for _ in range(20)]
    print(f"Unformatted dice rolls list: {dice_rolls}")
    print(f"Formatted dice rolls list: {' '.join(map(str, dice_rolls))}")       # ' '.join only works with string 

    # Find out the starting point and the length of the longest identical sequence
    start, length = find_longest_sequence(dice_rolls)
    formatted_result = format_with_parentheses(dice_rolls, start, length)
    print(f"Formatted result: {formatted_result}")

if __name__ == "__main__" :
    main()
