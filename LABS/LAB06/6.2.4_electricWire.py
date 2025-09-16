from math import pi 

COPPER_RESISTANCE = 1.678e-8 
ALUMINUM_RESISTANCE = 2.82E-8 


def diameter(wire_gauge) : 
    d = 0.127 * 92**((36-wire_gauge)/39)  # mm 
    return d / 1000     # m


def copper_wire_resistance(length, wire_gauge) : 
    d = diameter(wire_gauge)
    r = (4 * COPPER_RESISTANCE * length) / (pi * d**2)
    return r


def aluminum_wire_resistance(length, wire_gauge) : 
    d = diameter(wire_gauge)
    r = (4 * ALUMINUM_RESISTANCE * length) / (pi * d**2)
    return r


def main() : 
    length = float(input("Enter the length of a piece of wire(m): ")) 
    gauge = float(input("Enter the wire's gauge(AWG): ")) 

    print(f"For Copper wire, the resistance is {copper_wire_resistance(length, gauge):.3f} ohm") 
    print(f"For Aluminum wire, the resistance is {aluminum_wire_resistance(length, gauge):.3f} ohm") 
    
if __name__ == "__main__" : 
    main() 