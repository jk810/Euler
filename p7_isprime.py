def is_prime(x):
    prime = False
    if x > 1:
        prime = True
        k = 2
        n = x**0.5
        while k <= n and prime == True:
            if x % k == 0:
                prime = False
            k += 1
    return prime

primes = []
a = 0
b = 2
lim = 10001
while a < lim:
    if is_prime(b):
        primes.append(b)
        a += 1
    b += 1
print(primes[-1])
