from random import randint 

def main() : 
    #set up the starting configuration of the piles so that there will be exactly 45 cards 
    piles = [] 
    total = 0 

    while total < 45 : 
        current_pile = randint(1, 45-total) 
        total += current_pile 
        piles.append(current_pile)

    piles.sort()    #sort the piles 
    print("Initial configuration: ", end=" ")
    print(piles) 

    final_config = [1, 2, 3, 4, 5, 6, 7, 8, 9]        #from the question
    while piles != final_config :       #while we have not yet reached the final configuration 
        for i in range(0, len(piles)) : 
            piles[i] = piles[i] - 1     #remove one card from each file 
        
        #create a new pile made up of the cards subtracted from the starting piles
        piles.append(len(piles))

        #remove any size 0 piles from the list 
        while 0 in piles : 
            piles.remove(0) 
        
        #keep the piles sorted from smallest to largest 
        piles.sort() 

        #display the current configuration 
        print(piles)
    
if __name__ == "__main__" : 
    main() 