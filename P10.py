# Project Euler Problem 10
# Justin Kim
# Sum of all primes below 2 million

import time
start_time = time.time()

#def largest_PF(n):
#    i = 2
#    while i*i <= n:        # Smallest prime factor <= sqrt(n) unless n is prime
#        if n % i == 0:
#            n /= i
#        else:
#            i += 1
#    return n
#
#ans = 2
#for i in range(3, 2000000,2):
#    if largest_PF(i) == i:
#        ans += i


def sum_of_primes(limit):
    prime = [True] * limit
    total = 2

    for i in range(3, limit, 2):
        if prime[i]:
            total += i
            for multiple in range(i * i, limit, 2 * i):
                prime[multiple] = False

    return total


a = sum_of_primes(2000000)


elapsed_time = time.time() - start_time

print(a)

