import random 

SMART = 0 
DUMB = 1 

def humans_turn(n) :
    max_take = n//2 if n>1 else 1 

    while True : 
        try : 
            take = int(input(f"How many marbles do you want to take?(1~{max_take}): "))

            if 1 <= take <= max_take : 
                return n - take 
            else : 
                print(f"Invalid move. Choose between 1 and {max_take}.")
        except ValueError : 
            print("Please enter a valid number.")

def intelligent_mode(n) : 
    # List of target numbers: 2^k - 1 
    lst_target = [1, 3, 7, 15, 31, 63]  

    if n in lst_target :
        dumb_mode(n) 
        return
    
    for target in lst_target : 
        if target < n : 
            take = n - target

    print(f"Computer(smart) takes {take} marbles.")
    return n - take 

def dumb_mode(n) : 
    take = random.randint(1, n//2 if n>1 else 1)
    print(f"Computer(dumb) takes {take} marbles.")
    return n- int(take)

def main() : 
    initial_size = random.randint(10, 100)          # use case of random module and methods 
    player = random.choice([0, 1])              # 0 = computer, 1 = Human
    strategy = random.choice([SMART, DUMB])
    
    curr_marbles = initial_size
    print(f"\nInitial Pile size: {curr_marbles}") 
    print("Player to start:", "Computer" if player == 0 else "Human") 
    print("Computer strategy:", "SMART" if strategy == SMART else "DUMB")
    print()

    while curr_marbles > 1 : 
        print(f"\nMarbles left: {curr_marbles}")

        if player == 0:     # computer's turn
            print("Computer's Turn!")
            if strategy == DUMB : 
                curr_marbles = dumb_mode(curr_marbles)
            else : 
                curr_marbles = intelligent_mode(curr_marbles)
                        
            player = 1      # update player

        else :      # Human's turn
            print("Human's Turn!")
            curr_marbles = humans_turn(curr_marbles)
            player = 0      # update player

    if player == 0 : 
        print("\nComputer took the last marble. You won!") 
    else :
        print("\nHuman took the last marble. Computer won!")

if __name__ == "__main__" : 
    main()