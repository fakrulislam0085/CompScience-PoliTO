# Define constant variables - From the question
INITIAL_DISPLACEMENT = 0.5  # m 
INITIAL_VELOCITY = 0    # m/s 
MASS = 1    # kg 
K = 10  # N/m 
TIMESTEP = 0.01 # s 

def main() : 

    x = INITIAL_DISPLACEMENT 
    v = INITIAL_VELOCITY 
    delta_t = TIMESTEP
    t = 0   # time 

    while t < 1.0 : 
        F = - K * x 
        a = F / MASS    # F = ma
        v = v + a * delta_t 
        x = x + v * delta_t 
        print(f'Time = {t:5.2f} s       position = {x:8.3f} m')
        t = t + delta_t     # update the time

if __name__ == "__main__" : 
    main() 
