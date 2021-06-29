n = 600851475143

i = 2
while i * i <= n:
    if n % i != 0:
        i += 1
    else:
        n //= i
print(n)


def prime_factors(n):
    pfs = []
    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            pfs.append(i)
    pfs.append(n)
    return pfs

def largest_pf(n):
    i = 2
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
    return n