''' 
Lists can be used to store data in two dimensions (2D) like a spreadsheet:
* Rows and Columns
* Also known as a 'matrix'

Technically, we will build tables as lists of lists:
* Lists whose elements are other lists

'''
#using row-coloumn to create a table
rows = 3 
columns = 2 
table = []

for i in range(rows) :
    row = [0] * columns 
    table.append(row)

print(table)


#compact version - only works for constant initialization
rows = 4 
columns = 3 
table = [[5] * columns] * rows 
print(table)



#manual way to create a table
counts = [ [0, 3, 1],
           [0, 0, 1],
           [0, 0, 1],
           [1, 0, 0], 
           [0, 1, 0], 
           [3, 1, 1],
           [1, 1, 1], 
           [1, 3, 1] ]
print(counts)

print(counts[3][1])     #accessing elements = table[row][column]

#print the i th row
i = 3   #4th row
print("i-th row:", end = ' ')
for j in range(3) :     #total columns = 3
    print(counts[i][j], end = ' ')

#print the j th column 
print("\nj-th column:", end = ' ')
j = 2  #3rd column
for i in range(8) :     #total rows = 8
    print(counts[i][j], end = ' ')


