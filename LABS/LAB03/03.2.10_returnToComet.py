''' 
If the person jumps slower than escape velocity → they return.
If the person jumps faster than escape velocity → they escape and don't return.
If they escape, we need to find how much more mass the comet should have so they don't 
escape with that speed.
'''
import math 

G = 6.67e-11    # 6.67 * 10^-11 N m^2 kg^-2
M = 2.2e14      # 2.2 * 10^14 kg 
D = 9.4         # diameter of 9.4 km 
R = 4.7e3       # R = D/2 km

def main() : 
    launch_velocity_kmph = float(input("Enter your launch velocity(in Km/hr): "))
    launch_velocity_mps = launch_velocity_kmph * 1000/3600 

    # Calculating escape velocity 
    escape_velocity = math.sqrt((2 * G * M) / R)

    print(f"\nEscape velocity from Halley's Comet: {escape_velocity:.2f} m/s")
    print(f"Your launch speed: {launch_velocity_mps:.2f} m/s") 

    if launch_velocity_mps < escape_velocity : 
        print("You will return to the surface of the comet.")
    else : 
        # Calculate how much mass would be needed to prevent escape 
        required_mass = ((launch_velocity_mps ** 2) * R) / (2 * G)
        extra_mass = required_mass - M 
        print("You will escape the Comet.")
        print(f"The Comet would need {extra_mass:.2f} kg more mass to pull you back.")

if __name__ == "__main__" : 
    main() 