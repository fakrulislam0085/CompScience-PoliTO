# This program solves the exercise building two tables, one per robot, with 1s
# in positions touched by the robot, and 0s elsewhere. It is more intuitive
# but a little bit longer than the sets alternative. It has the advantage of
# allowing you to visualize the paths (with the printTable function, that I
# commented out as printing the paths was not requested).

SIZE = 10


def main():
    robot1 = input("Give me the name of the first robot:")
    robot2 = input("Give me the name of the second robot:")
    tables = []
    with open("trajectories.txt", "r") as f:
        for line in f:
            line = line.strip()
            name, x, y, path = line.split()
            x = int(x) - 1
            y = int(y) - 1
            if name == robot1 or name == robot2:
                robot_table = buildTable(x, y, path)
                # print("Robot:", name)
                # printTable(robot_table)
                tables.append(robot_table)
    if len(tables) != 2:
        print("I couldn't find some of the robots in the file")
    else:
        countShared = 0
        for i in range(SIZE):
            for j in range(SIZE):
                if tables[0][i][j] == 1 and tables[1][i][j] == 1:
                    countShared += 1
        print("The number of locations touched by both robots is:", countShared)


def printTable(table):
    for i in range(SIZE):
        for j in range(SIZE):
            print(table[i][j], end='')
        print()


def buildTable(x, y, path):
    # make a table of 0s of dimension SIZE x SIZDE
    table = []
    for i in range(SIZE):
        table.append([0] * SIZE)
    # mark the starting position
    table[x][y] = 1

    # process one movement at a time
    for j in range(0, len(path), 2):
        # update x, y coordinates
        sign = path[j]
        direction = path[j+1]
        if sign == '+' and direction == 'v':
            x = x + 1
        elif sign == '+' and direction == 'h':
            y = y + 1
        elif sign == '-' and direction == 'v':
            x = x - 1
        else:
            y = y - 1
        # mark the new position
        table[x][y] = 1
    return table


main()
