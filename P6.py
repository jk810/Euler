import numpy as np

a = np.arange(1, 101)
b = sum(a**2) - sum(a)**2
print(b)