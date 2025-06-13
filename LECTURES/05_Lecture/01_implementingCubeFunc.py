"""
This script calculates the volume of a cube given its side length and demonstrates its usage.

Functions:
1. cubeVolume(sidelength):
   - Computes the volume of a cube using the formula: volume = sidelength ** 3.
   - Returns the calculated volume.

2. main():
   - Demonstrates the cubeVolume function by calculating the volumes of cubes with side lengths 2, 4, and 10.
   - Prints the results in a formatted manner.
"""
def cubeVolume(sidelength) : 
    volume = sidelength ** 3
    return volume 

def main():
    result1 = cubeVolume(2)
    result2 = cubeVolume(4)

    print("A cube with side length 2 has volume:",result1)
    print("A cube with side length 4 has volume:",result2)
    print("A cube with side length 10 has volume:",cubeVolume(10))
    
main()