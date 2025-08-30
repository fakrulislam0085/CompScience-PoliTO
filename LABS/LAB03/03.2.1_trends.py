def main() : 
    x, y, z = map(float, input("Enter three real numbers(separated by space): ").split())

    if x>y>z :  # Comparison Chaining is allowed in Python [read more in README.md file]
        print("They are strictly decreasing!")
    elif x<y<z : 
        print("They are strictly increasing!") 
    else :
        print("They are neither in increasing order nor decreasing order.")

if __name__ == "__main__" : 
    main() 