import math 

def sphere_volume(r) : 
    return 4/3 * math.pi * r**3

def sphere_surface(r) :
    return 4 * math.pi * r ** 2 

def cylinder_volume(r, h) :
    return math.pi * r**2 * h 

def cylinder_surface(r, h) :
    return 2 * (math.pi * r**2 + math.pi * r * h)

def cone_volume(r, h) :
    return 1/3 * math.pi * r**2 * h 

def cone_surface(r, h) :
    s = math.sqrt(r**2 + h**2) 
    return math.pi * r * s + math.pi * r**2

def main() : 
    r = float(input("Enter the radius: ")) 
    h = float(input("Enter the height: "))

    print(f"A sphere with radius {r} has a volume of {sphere_volume(r)} meter^3")
    print(f"A sphere with radius {r} has a surface of {sphere_surface(r)} meter^2")
    print(f"A cylinder with radius {r} and height {h} a volume of {cylinder_volume(r, h)} meter^3") 
    print(f"A cylinder with radius {r} and height {h} a surface of {cylinder_surface(r, h)} meter^2") 
    print(f"A cone with radius {r} and height {h} a volume of {cone_volume(r, h)} meter^3") 
    print(f"A cone with radius {r} and height {h} a surface of {cone_surface(r, h)} meter^2") 

if __name__ == "__main__" : 
    main()