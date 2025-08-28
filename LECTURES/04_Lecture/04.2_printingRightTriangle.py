side = int(input("Enter the max side length: "))

#upper right triangle
print("upper right triangle: ", end='\n')
for i in range(1, side + 1) :
    print(i * '*')


#lower right triangle
print()
print("lower right triangle: ", end='\n')
for i in range(side, 0, -1) :
    print(i * '*')


#Middle right triangle
print(f"\nMiddle right triangle: ")
space = side - 1
stars = 1
for i in range(side) :
    print(space * " ", stars * '*')
    space -= 1
    stars += 2


#Middle left Triangle
print(f"\nMiddle left Triangle: ")
space = 0
stars = side * 2 - 1
for i in range(side) :
    print(space * " ", stars * '*')
    space += 1
    stars -= 2


#Middle right void triangle
print(f"\nMiddle right void triangle: ")
space = side - 1
stars = 1

for i in range(side-1) :
    if i == 0:
        print(space * ' ' + stars * '*')
    else :
        print(space*' '+"*"+(stars-2) * ' '+"*")
    space -= 1
    stars += 2

print((side*2 - 1) * '*')       #print the last line



#Middle left void triangle
print(f"\nMiddle left void triangle: ")
print((side*2-1)*'*')   #print first line
space = 1
stars = (side*2-1) - 2

for i in range(1, side) :
    if i == side-1 :
        print(space * ' ' + '*')
    else :
        print(space*' ' + "*" + (stars-2)* ' ' + "*")
    stars -= 2
    space += 1