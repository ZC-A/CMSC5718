import numpy as np
import time

# Function to calculate the fair price of the option
def calculate_option_price_1(paths, steps):
    start_time = time.time()
    
    # Parameters
    S10 = 293.60 # Initial stock price S1 at t=0
    S20 = 43.2  # Initial stock price S2 at t=0
    alpha1 = 0.318
    alpha2 = 0.21
    r = 0.0523  # Continuously compounded interest rate
    T = 0.75  # Time to maturity in years
    
    dt = T / steps  # Time step size
    
    total_payoff = 0.0
    
    for _ in range(paths):   
        S1 = S10
        S2 = S20
        
        for _ in range(steps):
            # Generate random numbers
            z1 = np.random.standard_normal()
            z2 = np.random.standard_normal()
            
            # Calculate stock price changes
            deltaS1 = S1 * dt * r +  alpha1 * z1 * S1 * np.sqrt(dt) 
            deltaS2 = S2 * dt * r +  alpha2 * z2 * S2 * np.sqrt(dt) 
            
            # Update stock prices
            S1 += deltaS1
            S2 += deltaS2
        
        # Calculate A, B1, and B2
        B1 = max(S1 / S10, S2 / S20)
        B2 = max(S1 / S10, S2 / S20)
        A = (B1 + B2) / 2
        
        
        # Calculate payoff at maturity
        payoff = max(A - 1.0, 0.0)
        
        # Add payoff to total
        total_payoff += payoff
    
    # Calculate average payoff
    average_payoff = total_payoff / paths
    
    # Calculate fair price
    fair_price = average_payoff * np.exp(-r * T) * (S10 + S20)
    
    end_time = time.time()
    computation_time = end_time - start_time
    
    return fair_price, computation_time


# Set parameters
paths = 10000  # Number of paths
steps = 150  # Time steps
print("Q2_1:")
# Calculate option price with 10000 paths
price_10000, time_10000 = calculate_option_price_1(paths, steps)
print("Fair price of the option with 10000 paths:", price_10000 )
print("Computation time with 10000 paths:", time_10000, "seconds")

# Calculate option price with 300000 paths
paths = 300000  # Number of paths
price_300000, time_300000 = calculate_option_price_1(paths, steps)
print("Fair price of the option with 300000 paths:", price_300000)
print("Computation time with 300000 paths:", time_300000, "seconds")




# Function to calculate the fair price of the option
def calculate_option_price_2(paths, steps):
    start_time = time.time()
    
    # Parameters
    S10 = 293.60 # Initial stock price S1 at t=0
    S20 = 43.2  # Initial stock price S2 at t=0
    alpha1 = 0.318
    alpha2 = 0.21
    r = 0.0523  # Continuously compounded interest rate
    T = 0.75  # Time to maturity in years
    
    dt1 = 0.5 # Time step size
    dt2 = 0.25 # Time step size
    
    total_payoff = 0.0
    
    for _ in range(paths):   
        S1 = S10
        S2 = S20
        
        #dt1
        # Generate random numbers
        z1 = np.random.standard_normal()
        z2 = np.random.standard_normal()
        # Calculate stock price changes with dt1
        deltaS1 = S1 * dt1 * r +  alpha1 * z1 * S1 * np.sqrt(dt1) 
        deltaS2 = S2 * dt1 * r +  alpha2 * z2 * S2 * np.sqrt(dt1) 
        # Update stock prices
        S1 += deltaS1
        S2 += deltaS2    
        #dt2
        # Generate random numbers
        z1 = np.random.standard_normal()
        z2 = np.random.standard_normal()
        # Calculate stock price changes with dt1
        deltaS1 = S1 * dt2 * r +  alpha1 * z1 * S1 * np.sqrt(dt2) 
        deltaS2 = S2 * dt2 * r +  alpha2 * z2 * S2 * np.sqrt(dt2) 
        # Update stock prices
        S1 += deltaS1
        S2 += deltaS2  

        # Calculate A, B1, and B2
        B1 = max(S1 / S10, S2 / S20)
        B2 = max(S1 / S10, S2 / S20)
        A = (B1 + B2) / 2
        
        
        # Calculate payoff at maturity
        payoff = max(A - 1.0, 0.0)
        
        # Add payoff to total
        total_payoff += payoff
    
    # Calculate average payoff
    average_payoff = total_payoff / paths
    
    # Calculate fair price
    fair_price = average_payoff * np.exp(-r * T) * (S10 + S20)
    
    end_time = time.time()
    computation_time = end_time - start_time
    
    return fair_price, computation_time


# Set parameters
paths = 10000  # Number of paths
steps = 150  # Time steps
print("Q2_2:")
# Calculate option price with 10000 paths
price_10000, time_10000 = calculate_option_price_2(paths, steps)
print("Fair price of the option with 10000 paths:", price_10000 )
print("Computation time with 10000 paths:", time_10000, "seconds")

# Calculate option price with 300000 paths
paths = 300000  # Number of paths
price_300000, time_300000 = calculate_option_price_2(paths, steps)
print("Fair price of the option with 300000 paths:", price_300000)
print("Computation time with 300000 paths:", time_300000, "seconds")
