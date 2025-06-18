#p6.35
#function to print the flood Map 
def floodMap(heights, waterLevel) :
    for row in heights :
        for eachHeight in row :
            if eachHeight <= waterLevel :
                print("~", end = " ")
            else :
                print(" ", end=" ")
        print()
        
#function to show how the terrain gets flooded in ten steps
def showFlooding(heights) :
    #calculate the min and max heights in the terrain
    min_height = min(min(row) for row in heights)
    max_height = max(max(row) for row in heights)

    #calculate the step size
    step = (max_height - min_height) / 10 

    #iterate through each step 
    for i in range(11) :
        waterLevel = min_height + i * step
        print(f"Water level: {waterLevel:.2f}")
        floodMap(heights, waterLevel)
        print()

#heights table
heights = [[3, 3, 4],
           [6, 3, 5],
           [2, 4, 1]
           ]
# waterLevel = 5

# floodMap(heights, waterLevel)

#show flooding in ten steps
showFlooding(heights)



#page 107-112 summary (Read it before exam)