def park_car(parking_row):
    # Find the longest sequence of False (free spaces)
    max_length = 0
    start_index = 0
    current_length = 0

    # Iterate through the parking row to find the longest empty segment
    for i in range(len(parking_row)):
        if parking_row[i] == False:
            current_length += 1
        else:
            # When we encounter a True, reset the current segment length
            if current_length > max_length:
                max_length = current_length
                start_index = i - current_length
            current_length = 0

    # If the last segment ends as the longest, check that as well
    if current_length > max_length:
        max_length = current_length
        start_index = len(parking_row) - current_length

    # Park the car in the middle of the longest segment
    middle_index = start_index + (max_length // 2)
    parking_row[middle_index] = True  # Mark this spot as occupied

def display_parking_row(parking_row):
    # Display the parking row, where False is a free space and True is an occupied space
    print(" ".join(['X' if occupied else '_' for occupied in parking_row]))

def main():
    n = int(input("Enter the number of parking spaces: "))
    parking_row = [False] * n  # Initialize all parking spaces as free (False)
    
    # Simulate parking
    while parking_row.count(False) > 0:
        park_car(parking_row)
        display_parking_row(parking_row)


if __name__ == "__main__" : 
    main()