#%% Project Euler Problem 14
# Justin Kim
# Longest Collatz sequence from a starting number < 1000000

import time
start_time = time.perf_counter()
def collatz(n):
    count = 1
    while n > 1:
        if n % 2 == 0:
            n /= 2
            count += 1
        else:
            n = 3 * n + 1
            count += 1
    return count

count = 1

for i in range(800000, 1000000):
    if count < collatz(i):
        count = collatz(i)
        a = i


elapsed_time = time.perf_counter() - start_time
