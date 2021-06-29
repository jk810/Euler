# Project Euler Problem 24
# Justin Kim
# Millionth lexicographic permutation of digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

import time
import itertools

start = time.perf_counter()

print(list(itertools.permutations(range(10)))[999999])

elapsed = time.perf_counter() - start
print(elapsed)
