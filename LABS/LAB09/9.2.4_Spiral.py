def createASimpleTable(n) : 
    # Create a simple table of special value "None", we will convert this into a spiral table of nxn numbers
    table = [[None for j in range(n)] for i in range(n)] 

    return table 

def spiralTable(table, n) : 
    i = 0
    j = 0 
    count = 1 
    finalNum = n*n

    while count <= finalNum : 
        #Go right 
        while count <= finalNum and j<n and table[i][j] == None : 
            table[i][j] = count 
            count += 1 
            j += 1 
        
        #Go down 
        j -= 1  
        i += 1   
        while count <= finalNum and i<n and table[i][j] == None : 
            table[i][j] = count 
            count += 1
            i += 1 

        #Go left 
        i -= 1 
        j -= 1 
        while count <= finalNum and j>=0 and table[i][j] == None : 
            table[i][j] = count 
            count += 1 
            j -= 1 

        #Go up 
        j += 1 
        i -= 1 
        while count <= finalNum and i>=0 and table[i][j] == None : 
            table[i][j] = count 
            count += 1 
            i -= 1 

        #To go right again 
        i += 1 
        j += 1   
    
    return table

def printTheSpiralTable(table, n): 
    print(f"\nSpiral Table of {n}X{n}:")

    for i in range(n) : 
        for j in range(n) : 
            print(table[i][j], end=" ") 
        print()

def main() : 
    n = int(input("Enter an int to create a spiral table of (nxn) numbers: ")) 

    table = createASimpleTable(n) 
    table = spiralTable(table, n)   
    printTheSpiralTable(table, n) 


if __name__ == "__main__" :
    main() 