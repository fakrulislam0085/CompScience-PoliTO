def main() : 
    long_seq = input("Enter the long sequence of DNA(20 char): ").upper()
    short_seq = input("Enter the short sequence of DNA(3 char): ").upper()

    # Input validation 
    if(len(long_seq) != 20 or len(short_seq) != 3) : 
        print("Input characters is not correct!\nPlease Input again!")

    position = long_seq.index(short_seq) 
    times = long_seq.count(short_seq)

    if short_seq in long_seq : 
        print()
        print(f"I. The 'long sequence' contains the 'short sequence'.")
        print(f"II. Starting position of the 'short' seq within the long seq is: {position+1}")
        print(f"III. {short_seq} appears {times} time(s) in the {long_seq}")

    else: 
        print("I. The 'long sequence' does not contain the 'short sequence'.")

if __name__ == "__main__" :
    main() 