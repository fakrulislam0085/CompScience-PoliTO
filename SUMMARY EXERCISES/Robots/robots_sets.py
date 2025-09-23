# This program solves the exercise using two sets. It is probably
# the best solution, but a little bit less intuitive than the other.
SIZE = 10


def main():
    robot1 = input("Give me the name of the first robot:")
    robot2 = input("Give me the name of the second robot:")
    sets = []
    with open("trajectories.txt", "r") as f:
        for line in f:
            line = line.strip()
            name, x, y, path = line.split()
            x = int(x) - 1
            y = int(y) - 1
            if name == robot1 or name == robot2:
                robot_set = buildSet(x, y, path)
                # print("Robot:", name)
                # print(robot_set)
                sets.append(robot_set)
    if len(sets) != 2:
        print("I couldn't find some of the robots in the file")
    else:
        countShared = len(sets[0].intersection(sets[1]))
        print("The number of locations touched by both robots is:", countShared)


def buildSet(x, y, path):
    robot_set = set()
    # add starting position
    robot_set.add((x, y))
    # go over sting one movement (2 chars) at a time
    for j in range(0, len(path), 2):
        # extract sign and direction
        sign = path[j]
        direction = path[j+1]
        # update x and y coordinates
        if sign == '+' and direction == 'v':
            x = x + 1
        elif sign == '+' and direction == 'h':
            y = y + 1
        elif sign == '-' and direction == 'v':
            x = x - 1
        else:
            y = y - 1
        # add new x, y coordinates to the set
        robot_set.add((x, y))
    return robot_set


main()
