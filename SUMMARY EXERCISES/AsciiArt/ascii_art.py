# The program has been fixed also to work on landscape2.txt and landscape3.txt
# The error was that I did not correct the rstrip() in line 16, but just in
# line 12

from operator import itemgetter


# Read the file as a list of strings so that you can access every character as:
# land[i][j]
def readLandscape(filename):
    land = []
    try:
        with open(filename, 'r') as f:
            firstLine = f.readline()
            firstLine = firstLine.rstrip('\n')
            ncol = len(firstLine)
            land.append(firstLine)
            for line in f:
                line = line.rstrip('\n')
                if len(line) != ncol:
                    print("Error! Not all columns have the same length")
                    exit()
                land.append(line)
    except FileNotFoundError:
        print("Cannot open landscape")
        exit()

    nrow = len(land)
    return land, nrow, ncol


# Compute the number of occurrences of each character in the square
def computeStats(land, y, x, size, nrow, ncol):
    stats = {}
    for i in range(y, y + size):
        for j in range(x, x + size):
            c = land[i][j]
            if c not in stats:
                stats[c] = 0
            stats[c] += 1
    return stats


def printStats(stats, sum):
    its = stats.items()
    # [(l1, o1), (l2, o2), (l3, o3), ...]
    its = sorted(its, key=itemgetter(1), reverse=True)

    # alternative if you don't realise that the total number of characters
    # in the sequare is simply size * size
    # sum = 0
    # for l, o in its:
    #     sum += o

    for let, o in its:
        pct = (o / sum) * 100
        print(f"{let}-> {pct:4.1f}%")


def main():
    land, nrow, ncol = readLandscape('landscape3.txt')
    coords = input("Please, enter the coordinates (x,y):")
    x, y = coords.split(',')
    size = input("Please, enter the square size:")
    try:
        x = int(x)
        y = int(y)
        size = int(size)
    except ValueError:
        print("I cannot convert coordinates or size to integers")
        exit()

    if size <= 0:
        print("Invalid negative size")
        exit()
    
    # check if square is valid
    if 0 <= x < ncol - size and 0 <= y < nrow - size:
        stats = computeStats(land, y, x, size, nrow, ncol)
        # TODO: print the stats
        printStats(stats, size*size)
    else:
        print("ERROR!! the square to analyze is out of limits.")


main()