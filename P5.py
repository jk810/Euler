import math
import numpy as np

a = math.factorial(20)
b = np.arange(1, 21)

d = 2*3*5*7*11*13*17*19

k = 1
while d < a:
    d *= k
    c = d % b
    if all(j == 0 for j in c):
        print(d)
        break
    else: k += 1