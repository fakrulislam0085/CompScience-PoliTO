#initial table 
table = [ [0, 3, 1],
          [0, 0, 1],
          [0, 0, 1],
          [1, 0, 0], 
          [0, 1, 0], 
          [3, 1, 1],
          [1, 1, 1], 
          [1, 3, 1] ]

#function to sum elements of a specific row
def sum_row(table, row_index) :
    total = 0 
    for element in table[row_index] :
        total += element
    return total

#function to sum elements of a specific column 
def sum_column(table, column_index) :
    total = 0 
    for row in table :
        total += row[column_index]
    return total 

#summing elements of the 4th row (index = 3) 
row_index = 3 
row_sum = sum_row(table, row_index)
print(f"Sum of elemenets in row {row_index + 1} = {row_sum}")

#summing elements of the 3rd column(index = 2) 
col_indx = 2 
row_col = sum_column(table, col_indx)
print(f"Sum of elements in column {col_indx+1} = {row_col}")
