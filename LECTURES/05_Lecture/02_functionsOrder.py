"""
This script calculates the volume of a cube using the cubeVolume function and 
demonstrates its usage in the main function.
"""
def main():
    sidelength = 5
    result = cubeVolume(sidelength)
    print("Volume of a cube with side length 5 is", result)
    
def cubeVolume(sidelength) :
    return sidelength ** 3

main()