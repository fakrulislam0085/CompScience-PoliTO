def main() : 
    R1, R2, R3 = map(float, input("Enter the Resistance(in ohm): ").split()) 

    # Resistance = parallel resistance + series resistance 
    # R2 and R3 resistances are parallel: 1/Rtotal = 1/R2 + 1/R3 
    Rp = 1/((1/R2) + (1/R3)) 

    # R1 and Rp are series: Rtotal = R1 + Rp
    Rs = R1 + Rp 

    R_total = Rs 
    print(f"The total resistance of the circuit is {R_total} ohm")

if __name__ == "__main__" : 
    main()