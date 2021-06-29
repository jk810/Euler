#%% Project Euler Problem 7
# Justin Kim
# What is the 10001st prime number

import time
start_time = time.time()

def largest_PF(n):
    i = 2
    # Smallest prime factor <= sqrt(n) unless n is prime
    while i*i <= n:
        if n % i == 0:
            n /= i
        else:
            i += 1
    return n

i = 2
count = 1

while count <= 10001:
    if largest_PF(i) == i:
        count += 1
    i += 1

ans = i - 1


elapsed = time.time() - start_time