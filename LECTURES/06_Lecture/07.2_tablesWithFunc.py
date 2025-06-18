#initial table
table = [ [0, 3, 1],
          [0, 0, 1],
          [0, 0, 1],
          [1, 0, 0], 
          [0, 1, 0], 
          [3, 1, 1],
          [1, 1, 1], 
          [1, 3, 1] ]

#using two for loops to sum all elements of the table  #1st approach
def summation(table) :
    total = 0 
    for i in range(len(table)) :
        for j in range(len(table[i])) :
            total += table[i][j]
    return total
print("Total value of the table:", summation(table))



#function to calculate the total value of the table    #2nd approach
def calculate_total(table) :
    total = 0
    for row in table :
        for element in row :
            total += element 
    return total
print("Total value of the table:", calculate_total(table))



#function to calculate the total value of the table     #3rd approach
def total_val(table) :
    total = 0 
    for row in table :
        total += sum(row) 
    return total
print("total of the table:", total_val(table))

