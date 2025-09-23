def main() : 
    print("Welcome to Unit Converter\n") 

    # Volume units 
    volume_units = {'ml': 1, 'l':1000, 'fl':29.5735, 'oz':29.5735, 'gal':3785.41}

    # Weight/mass units 
    mass_units = {'g': 1, 'kg':1000, 'oz':28.3495, 'lb':453.592} 

    # Distance units 
    length_units = {'mm': 0.001, 'cm':0.01, 'm':1, 'km':1000, 'in':0.0254, 'ft':0.3048, 'mi':1609.34}

    all_units = {**volume_units, **mass_units, **length_units}          # what is this approach? 

    
    from_unit = input("Convert from? (ml, l, g, kg, mm, cm, m, km): ") 
    to_unit = input("Convert to? (fl, oz, gal, oz, lb, in, ft, mi): ")

    if from_unit not in all_units or to_unit not in all_units :
        print("Invalid unit entered.")
        return 
    
    # Check compatibility 
    if (from_unit in volume_units and to_unit not in volume_units) or \
        (from_unit in mass_units and to_unit not in mass_units) or \
        (from_unit in length_units and to_unit not in length_units) :
        print("Incompatible units! Can't convert between volume/mass/length.")
        return

    try : 
        value = float(input("Enter the value to convert: ")) 
    except ValueError : 
        print("Please enter a valid number.")
        return
    
    # Convert to base (ml, g, m), then to target
    base_value = value * all_units[from_unit]
    converted = base_value / all_units[to_unit]

    print("Conversion results:")
    print(f"{value} {from_unit} = {converted:.2f} {to_unit}")

if __name__ == "__main__" : 
    main() 



