from random import randint

def main() : 
    x, y = 0, 0     # Starting position 

    # Assign a number to each direction 
    Up, down = 0, 1 
    left, right = 2, 3

    for _ in range(100) :       # Total 100 intersections 
        direction = randint(0, 4) 

        if direction == Up :
            y += 1
        elif direction == down : 
            y -= 1
        
        elif direction == right : 
            x += 1
        elif direction == left :
            x -= 1

    total_distance = abs(x) + abs(y) 
    print(f"The drunk man ended up at ({x},{y}) position.") 
    print(f"The man's total distances from (0,0) is {total_distance}.")

if __name__ == "__main__" : 
    main() 
