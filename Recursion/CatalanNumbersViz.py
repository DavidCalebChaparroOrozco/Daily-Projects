# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import time
import pandas as pd
import numpy as np
from math import factorial, comb
from functools import lru_cache

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Calculate the nth Catalan number using a recursive approach with memoization.
@lru_cache(None)
def catalan_recursive(n):
    if n <= 1:
        return 1
    return sum(catalan_recursive(i) * catalan_recursive(n - i - 1) for i in range(n))

# Calculate the nth Catalan number using binomial coefficients.
def catalan_binomial(n):
    return comb(2 * n, n) // (n + 1)

# Plot the growth of Catalan numbers with a polynomial trend line.
def visualize_catalan_growth(max_n=20):
    x = np.arange(max_n + 1)
    y = np.array([catalan_binomial(n) for n in x])
    
    plt.figure()
    sns.scatterplot(x=x, y=y, color='blue', label='Catalan Numbers')
    
    # Ajuste polinómico
    coefficients = np.polyfit(x, np.log(y), 2)
    poly_eq = np.exp(np.polyval(coefficients, x))
    plt.plot(x, poly_eq, linestyle='dashed', color='red', label='Polynomial Fit')
    
    plt.yscale('log')
    plt.xlabel('n')
    plt.ylabel('Catalan Number (log scale)')
    plt.title('Growth of Catalan Numbers')
    plt.legend()
    plt.show()

# Compare the values of Catalan numbers computed by different methods.
def compare_methods(max_n=15):
    data = {
        "n": list(range(max_n + 1)),
        "Binomial": [catalan_binomial(n) for n in range(max_n + 1)],
        "Recursive (Memoized)": [catalan_recursive(n) for n in range(max_n + 1)]
    }
    df = pd.DataFrame(data)
    df.set_index("n", inplace=True)
    
    plt.figure()
    df.plot(kind='bar', colormap='viridis', alpha=0.7)
    plt.title('Comparison of Catalan Number Methods')
    plt.ylabel('Catalan Number')
    plt.xlabel('n')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
# Run visualizations
visualize_catalan_growth(20)
compare_methods(15)
