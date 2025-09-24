def readFile(fileName, row, column, tab):
    fin = open(fileName, 'r')
    color = 0
    rowCount = 0
    count = 0
    for line in fin:
        columnCount = 0 
        for character in line: 
            if character.isdigit():
                tab[row + rowCount][column + columnCount] = int(character)
                color = color + int(character)
                count = count + 1
            columnCount = columnCount + 1
        rowCount = rowCount + 1
    fin.close()
    return(color/count, rowCount * columnCount)

def printTable(tab): 
    print()
    for line in tab: 
        for character in line: 
            print(character, end = '')
        print()

def main(): 
    picture = []
    for i in range(10):
        row = [9]*10
        picture.append(row)
        
    fin = open('input.txt','r')
    colors = []
    sizes = []
    for line in fin:
        fields = line.split()
        (color, size) = readFile(fields[0], int(fields[1]), int(fields[2]), picture)
        colors.append([color, fields[0]])
        sizes.append([size, fields[0]])

    fin.close()
    print(f'Numero file di immagini di input: {len(colors)}')
    print(f'Immagine più grande: {max(sizes)[1]}')
    print(f'Immagine più scura: {min(colors)[1]} {min(colors)[0]:.2f}')
    printTable(picture)
   
main()
