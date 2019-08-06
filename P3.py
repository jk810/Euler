#%% Project Euler Problem 3
# Justin Kim
# Largest prime factor

import time
start = time.time()

def primeFactorization(n):
    List = []
    i = 2

    # Smallest prime factor <= sqrt(n) unless n is prime
    while i*i <= n:
        if n % i == 0:
            n /= i
            List.append(i)
        else:
            i += 1
    List.append(n)

    return List


primeList = primeFactorization(600851475143)
largest = max(primeList)


elapsed = time.time() - start