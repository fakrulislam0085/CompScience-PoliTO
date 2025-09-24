# FILENAME = "expressions.dat"
FILENAME = "expressions_long.dat"


def main():
    # you can also process the expressions while reading them
    expressions = readExpressions(FILENAME)
    for expression in expressions:
        print(processExpression(expression))


def readExpressions(filename):
    expressions = []
    with open(filename, "r") as file:
        for line in file:
            try:
                operands, operators = line.strip().split(":")
                # parse operands
                operands = operands.strip().split(" ")
                for i in range(len(operands)):
                    operands[i] = int(operands[i])

                # parse operators
                operators = operators.strip().split(" ")
                for i in range(len(operators)):
                    if operators[i] not in ["+", "-", "*"]:
                        raise ValueError("Invalid operator")

                # check lengths
                if len(operands) != len(operators) + 1:
                    raise ValueError("Invalid number of operands and operators")

            except ValueError:
                print("Invalid expression found, terminating")
                exit()
            # also a list of tuples or a list of lists could have been used. This is more readable.
            expressions.append({"operands": operands, "operators": operators})
    return expressions


def processExpression(expression):
    a = expression["operands"].pop(0)
    while len(expression["operands"]) > 0:
        b = expression["operands"].pop(0)
        op = expression["operators"].pop(0)
        if op == "+":
            a = a + b
        elif op == "-":
            a = a - b
        elif op == "*":
            a = a * b
    return a


# alternative to the previous function, perhaps more "clear"
def processExpressionV2(expression):
    res = expression["operands"][0]
    for i in range(len(expression["operators"])):
        if expression["operators"][i] == "+":
            res += expression["operands"][i + 1]
        elif expression["operators"][i] == "-":
            res -= expression["operands"][i + 1]
        elif expression["operators"][i] == "*":
            res *= expression["operands"][i + 1]
    return res


main()
