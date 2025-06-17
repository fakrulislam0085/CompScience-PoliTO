'''We can fill a list using a loop (based on the criterion determined by
the specific problem) and the append() method.'''

n = int(input())
squares = []

for i in range(n) :
    squares.append(i*i)
print(squares)



#filling a list with user input
values = []
userInput = input("Please insert values or enter to quit:")

while userInput != "" :
    values.append(float(userInput))
    userInput = input("Please insert values or enter to quit:")
print(values)