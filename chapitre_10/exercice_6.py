from scipy.integrate import quad 
import matplotlib.pyplot as plt
import numpy as np

# Calculate integrale e^(-x^2) between -infinity and infinity 
def f(x):
    return np.exp((-1*x) ** 2)

integrale, err = quad(f, 1*np.inf, np.inf)
print(f"Integrale: {integrale} Error: {err}")

# Display integrale e^(-x^2) between -4 and 4
x = np.arange(-4, 4, 0.001)

plt.figure(figsize=(12,6))
plt.plot(x, f(x))
plt.title('e^(-x^2)')
plt.show()
