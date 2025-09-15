A = 2.5     # A = projected area (m^2)
d = 1.23    # d = Density of the air (kg/m^3)
Cd = 0.2    # Cd = drag coefficient 

WATTS_TO_HP = 1/746

def drag_force(v) : 
    Fd = 0.5 * Cd * v**2 *A * Cd    # Fd = 1/2(density * v^2 * A * Cd)
    return Fd 

def power(v) : 
    p = drag_force(v) * v   # P = Fd * V 
    return p

def main() : 
    kmh = float(input("Enter the speed of the car(kmh): ")) 
    V = (kmh * 1000) / 3600    # convert the speed in m/s 

    # Compute the power in Watts and Horse Power 
    p = power(V) 
    hp = p * WATTS_TO_HP

    print(f"To overcome the resulting drag force({drag_force(V):.2f}), the car needs {p:.2f} watts or {hp:.2f} Horsepower")


if __name__ == "__main__" : 
    main()



   