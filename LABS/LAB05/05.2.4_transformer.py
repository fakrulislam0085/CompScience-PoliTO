# We are not talking about Transformer Movie guys!
R0 = 20     # ohm
VS = 40     # Volt
RS = 8      # ohm

def main() : 
    max_power = -1 
    max_turns_ratio = -1

    n = 0.01    # turns ratio
    while n <= 2.0 :
        Ps = RS * (n * VS / (n**2 * R0 + RS))**2

        if Ps > max_power : 
            max_power = Ps 
            max_turns_ratio = n 

        n += 0.01

    print(f"The maximum power is {max_power:.2f} with turns ratio of {max_turns_ratio:.2f}")

if __name__ == "__main__" : 
    main() 
