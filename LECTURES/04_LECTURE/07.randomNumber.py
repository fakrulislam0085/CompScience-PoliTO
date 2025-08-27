#This program simulates tosses of a pair of dice
'''
Dice Toss Simulation: 
This program simulates the rolling of two six-sided dice 10 times. For each roll, 
it generates two random numbers between 1 and 6, representing the outcome of each die. 
The results of each roll are printed on the screen.

How It Works:
The program imports the randint function from Python's random module to generate random numbers.
A for loop runs 10 times to simulate 10 rolls. 
In each iteration:
Two random numbers (d1 and d2) are generated, simulating two dice rolls.
The results of the rolls are printed together
'''


from random import randint

for i in range (10) :
    #randint(a, b) generates a random integer between a and b (inclusive).
    d1 = randint(1, 6)  
    d2 = randint(1, 6) 

    #print two values
    print(d1, d2)

    #print the sum of two random values
    print(d1, d2, "Sum:", d1 + d2)
    
    #print the double values
    if d1 == d2:
        print("Doubles:", d1, d2)
