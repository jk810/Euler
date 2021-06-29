#%% Project Euler Problem 9
# Justin Kim
# Pythag triplet: a^2 + b^2 = c^2. Find triplet such that a + b + c = 1000

import time
start = time.time()

import numpy as np

for b in range(1000):
    for a in range(1000):
        c = (a**2 + b**2)**.5
        if (c).is_integer() and a < b < c and a + b + c == 1000:
            pythagtrip = np.array([a, b, c])

ans = np.product(pythagtrip)

elapsed = time.time() - start