# Project Euler Problem 15
# Justin Kim
# 20x20 lattice paths moving right or down

import math

def nCk(n,k):
    f = math.factorial
    return f(n) / f(k) / f(n - k)

# Any path from top left to bottom right consists of n steps right, 
# n steps down. So from 2n steps, we choose n, giving 2nCn

n = 20
n_paths = int(nCk(2*n,n))

print(n_paths)
