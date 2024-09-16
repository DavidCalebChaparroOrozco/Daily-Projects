# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Function to estimate the value of pi using the Monte Carlo method
# n: number of points generated per experiment
# n_exp: number of experiments to perform
def pi_montecarlo(n, n_exp):
    # Variable to store the average value of pi over all experiments
    pi_avg = 0  
    # List to store the value of pi from each experiment
    pi_value_list = []  

    # Loop over the number of experiments
    for i in range(n_exp):
        # Variable to count the points inside the unit circle
        value = 0  

        # Generate n random points for x and y coordinates between 0 and 1
        x = np.random.uniform(0, 1, n).tolist()
        y = np.random.uniform(0, 1, n).tolist()

        # Check if each point is inside the unit circle
        for j in range(n):
            # Distance from origin
            z = np.sqrt(x[j] * x[j] + y[j] * y[j])  
            if z <= 1:
                # Increment the count if the point is inside the circle
                value += 1  

        # Calculate the estimated value of pi for this experiment
        float_value = float(value)
        # Formula for estimating pi
        pi_value = float_value * 4 / n  
        # Append this value to the list
        pi_value_list.append(pi_value)  
        # Add the value to the total sum of pi values
        pi_avg += pi_value  

    # Calculate the average value of pi over all experiments
    pi = pi_avg / n_exp
    # Print the average estimated value of pi
    print(pi)  

    # Plot the estimated value of pi from each experiment
    plt.plot(pi_value_list)
    plt.title('Estimated Pi Values over Experiments')
    plt.xlabel('Experiment Number')
    plt.ylabel('Estimated Pi')
    plt.show()  

    return pi, pi_value_list

# Call the function with 10000 points and 200 experiments
pi_montecarlo(10000, 200)
