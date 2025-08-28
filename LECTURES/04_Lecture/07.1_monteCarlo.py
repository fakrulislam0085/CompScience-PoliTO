#this program computes estimates of pi by simulating dart throws onto a square
''' 
Pi Estimation Using Monte Carlo Simulation :
This program estimates the value of 𝜋 using a Monte Carlo method. 
It simulates throwing random "darts" (points) onto a square and calculates 
the ratio of points that land inside a unit circle to the total number of points. 
This ratio is used to approximate π.
'''


from random import random

TRIES = 10000
HITS = 0

for i in range(TRIES) :
    #random() generate two floating-points numbers between 0.0(inclusive) and 1.0(exclusive)
    r1 = random()
    x = -1 + 2 * r1
    r2 = random()
    y = -1 + 2 * r2

    #check whether the point lies in the unit circle (radius = 1)
    if x*x + y*y <= 1 :     # for unit circle: x² + y² ≤  1
        HITS += 1
    '''the ratio hits/tries is approximately the same as the ratio
    circle area / square area = pi / 4 '''

piEstimate = 4.0 * HITS/TRIES
print("Estimate for pi:",piEstimate)