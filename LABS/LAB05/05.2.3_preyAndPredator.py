
def main() : 

    # As test inputs we can use: A=0.1, B=0.01, C=0.01, D=0.00002
    A = float(input("Enter the growth rate of prey- A: "))
    B = float(input("Enter the rate of destruction of prey by predators- B: "))
    C = float(input("Enter the mortality rate of predators- C: "))
    D = float(input("Enter the rate of increase in predators through the consumption of prey- D: "))

    prey = int(input("Enter the initial number of prey (1000 is a good choice): "))
    predators = int(input("Enter the initial number of predators (20 is a good choice): "))

    iterations = int(input("How many iterations?: ")) # 10 is good to test the code 
    
    for period in range(1, iterations+1) : 
        new_prey = prey * (1+A - B*predators) 
        new_predators = predators * (1-C + D*prey) 

        if round(new_prey) > 0 and round(new_predators) > 0 : 
            print(f"[PERIOD #{period}]: Predators := {round(new_predators)} vs prey := {round(new_prey)}")
        
        if round(new_prey) <= 0 : 
            print(f"Prey has been eleiminated...RIP!")
            exit(0) 
        
        elif round(new_predators) <= 0 : 
            print(f"Predators have been eliminated...Horray!")
            exit(0)

        prey = new_prey 
        predators = new_predators

if __name__ == "__main__" : 
    main() 



