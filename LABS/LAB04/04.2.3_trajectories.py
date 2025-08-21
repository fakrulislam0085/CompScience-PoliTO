# Simulate the motion of a projectile 
DELTA_T = 0.01      # Constant- From the question

v = float(input("Enter the initial velocity: ")) 
v0 = v 
count = 1   # Number of computation steps 
delta_s = v * DELTA_T 

while delta_s > 0 :   # Until the cannon ball falls to the ground
    if count % 100 == 0 : 
        t = count // 100 
        s = -0.5 * 9.81 * t**2 + v0 * t         # s(t) = -(0.5gt^2) + v0t
        print(f"At time {t} position is: {delta_s:.2f}m and velocity is {v:.2f}m/s. \
              (Exact formuala position is {s:.2f}m)") 

    # Update the position and the velocity  
    delta_s = delta_s + v * DELTA_T 
    v = v - 9.81 * DELTA_T 
    count += 1 
