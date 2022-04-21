import numpy as np


def get_closest(array, value):
    absolute_differences = np.abs(array - value)
    return np.argmin(absolute_differences)


random_array = np.random.rand(1, 10)
bigger_random_array = np.array(random_array * 10)
value = 3.4

print(f"\nRandom array: \n {bigger_random_array} \n")
print(f"Closest value index: {get_closest(bigger_random_array, value)} \n")
