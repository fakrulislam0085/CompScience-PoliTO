# solution 2

def main() : 
    n = int(input("Total Parking spaces: ")) 

    occupied = []   #vacant list of occupied spaces
    for i in range(n) :
        occupied.append(False) 
    
    #Loop as long as there is at least one unoccupied slot 
    while False in occupied : 
        #Find the position and length of the longest sequence of unoccupied slots 
        longest_length = 0 
        longest_pos = 0 

        for i in range(len(occupied)) : 
            if not occupied[i]: 
                current_length = 1 
                pos = i + 1 

                while pos < len(occupied) and not occupied[pos] : 
                    current_length += 1
                    pos += 1
                
                if current_length > longest_length : 
                    longest_length = current_length 
                    longest_pos = i 

        #fill in the middle position in the longest unoccupied run
        occupied[longest_pos + longest_length//2] = True 

        #display the current status of the parking 
        for i in range(0, len(occupied)) : 
            if occupied[i] : 
                print("X", end="")
            else : 
                print("-", end="")
        print()

if __name__ == "__main__" : 
    main() 