def neighbor_average(values, row, col) :
    neighbor_sum = 0 
    neighbor_count = 0 

    for i in range(row-1, row+2) : 
        for j in range(col-1, col+2) : 
            if values[i][j] == values[row][col] : 
                continue 
            else : 
                neighbor_sum += values[i][j] 
                neighbor_count += 1 
    return neighbor_sum / neighbor_count 

def main() : 
    values = [] 
    r, c = map(int, input("Enter row and col: ").split()) 
    values = [[i+1 for j in range(c)] for i in range(r)] 

    for row in values : 
        '|'.join([f'{item:^5}' for item in row]) 
    
    print(values)

    print(f"The average at (0,0) is {neighbor_average(values, 0, 0):.2f}")
    print("The average at (1,2) is", neighbor_average(values, 1, 2))
    print("The average at (3,2) is", neighbor_average(values, 3, 2))

if __name__ == "__main__" : 
    main() 



