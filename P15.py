# in an nxn grid you have to move n times right and n times down
# total 2n moves: if you could go in any order, thre would be (2n)! routes
# but only moving right and down, it is 2n choose n:

import math

def lattice_paths(n):
    n_fact = math.factorial(n)
    return math.factorial(2 * n) / n_fact / n_fact

print(lattice_paths(20))