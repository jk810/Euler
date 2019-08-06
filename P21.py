# Project Euler Problem 21
# Justin Kim
# Amicable numbers

import time
import math

start = time.perf_counter()

def spd(n):
    s = 0
    for i in range(1, math.ceil(n/2) + 1):
        if n % i == 0:
            s += i
    return s

ans = 0
for i in range(200, 10000):
    x = spd(i)
    y = spd(x)
    if i == y and i != x:
        ans += i


elapsed = time.perf_counter() - start
