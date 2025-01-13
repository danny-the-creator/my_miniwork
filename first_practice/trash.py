import matplotlib.pyplot as plt
import numpy as np

# Data
xs = [0.00699305534362793, 0.008997440338134766, 0.021004199981689453, 0.019996166229248047, 0.021997690200805664]
gammas = [0.01, 0.1, 0.5, 0.9, 1.0]

# Create the decay curves
x = np.linspace(0, 60, 1000)  # X-axis range
for gamma in gammas:
    y = np.exp(-gamma * x)  # Exponential decay
    plt.plot(x, y, label=f'gamma={gamma}')

# Customize plot
plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Decay Curves for Different Gamma Values")
plt.grid()
plt.show()