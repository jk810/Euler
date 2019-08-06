#%% Project Euler Problem 12
# Justin Kim
# 1st triangle number to have >500 divisors

import time
start_time = time.time()

from itertools import groupby
import numpy as np


def primeFactorization(n):
    List = []
    i = 2
    while i*i <= n:     # Smallest prime factor <= sqrt(n) unless n is prime
        if n % i == 0:
            n /= i
            List.append(i)
        else:
            i += 1
    List.append(n)
    return List


numFac = 0
n = 1
while numFac < 500:
    tNumber = n*(n + 1)/2
    primeList = primeFactorization(tNumber)
    frequencyList = [len(list(group)) for key, group in groupby(primeList)]
    newFrequencyList = [x + 1 for x in frequencyList]

    numFac = np.product(newFrequencyList)
    n += 1

answer = tNumber

elapsed_time = time.time() - start_time
