import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 250)
y = np.array(((x ** 2) * np.sin(1/(x ** 2))) + x)

figure, axes = plt.subplots()
axes.plot(x, y)
plt.show()
