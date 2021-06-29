def nth_tri(n):
    # nth = 0
    # for i in range(n + 1):
    #     nth += i
    # return nth
    nth = n*(n + 1)/2
    return nth

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

def alphas(n):
    pfs = prime_factors(n)
    a = []
    uni = set(pfs)
    for i in uni:
        a.append(pfs.count(i))
    return a

def ndivs(n):
    ndivs = 1
    aa = alphas(n)
    for i in aa:
        ndivs *= (i + 1)
    return ndivs

c = 1
b = 1
while b < 500:
    nth = nth_tri(c)
    b = ndivs(nth)
    c += 1
print(nth)