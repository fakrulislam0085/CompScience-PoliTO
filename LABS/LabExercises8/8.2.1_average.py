def neighbor_average(values, row, column) : 
    total = 0       # to calculate the values of neighborhood cells 
    count = 0       # to count the total neighborhood cells 
    rows = len(values) 
    cols = len(values[0]) 

    for r in range(row-1, row+2) :      #row+2 exclusive so the loop will iterate over r-1, r, r+1
        for c in range(column-1, column+2) :    #column+2 exclusive so the loop will run c-1, c, c+1
            if r==row and c==column : 
                continue        # center cell 
            if (r>=0 and r<rows) and (c>=0 and c<cols) : 
                total += values[r][c] 
                count += 1 

    avg = total / count 
    return avg 

def main() : 
    # setup a samle 4x4 'values' table 
    valuesTable = [[1, 1, 1, 1], 
                   [2, 2, 2, 2], 
                   [3, 3, 3, 3], 
                   [4, 4, 4, 4]]

    for row in valuesTable:
        formatted_items = []  # create an empty list
        for item in row:
            formatted_item = f'{item:^5d}'  # format the number with center alignment in 5 spaces
            formatted_items.append(formatted_item)  # add it to the list
        print('|'.join(formatted_items))  # join all formatted strings with '|'

    # Demonstrate that neighbor average works correctly 
    print(f"The average at (0,0) is {neighbor_average(valuesTable, 0, 0):.2f}")
    print("The average at (1,2) is", neighbor_average(valuesTable, 1, 2))
    print("The average at (3,2) is", neighbor_average(valuesTable, 3, 2))

if __name__ == "__main__" : 
    main() 