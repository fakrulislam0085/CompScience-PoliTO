def main() : 
    wave_length = float(input("Enter the wave length: ")) 

    # Display the description of the radiation 
    if wave_length > 1e-1 :
        print("Radio Wave")
    elif 1e-3 <= wave_length < 1e-1 :
        print("Microwave")
    elif 7e-7 <= wave_length < 1e-3 : 
        print("Infared") 
    elif 4e-7 <= wave_length < 7e-7 : 
        print("Visible Light") 
    elif 1e-8 <= wave_length < 4e-7 : 
        print("Ultraviolet") 
    elif 1e-11 <= wave_length < 1e-8 : 
        print("X-rays") 
    elif wave_length < 1e-11 : 
        print("Gamma Rays") 
    
if __name__ == "__main__" : 
    main() 