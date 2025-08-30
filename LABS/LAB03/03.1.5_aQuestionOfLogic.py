def main():
    x = int(input("Enter an int: "))

    print(f"I.   x>0 and x<100           -> {str(x>0 and x<100):<5}")
    print(f"II.  x>0 or x<100            -> {str(x>0 or x<100):<5}")
    print(f"III. x>0 or 100<x            -> {str(x>0 or 100<x):<5}")
    print(f"IV.  x>0 and x<100 or x == -1-> {str(x>0 and x<100 or x == -1):<5}")

if __name__ == "__main__":
    main()
