n = 2000000
psum = 0
number = [1] * n
number[0] = number[1] = 0
for k in range(2, n):
    if number[k]:
        for j in range(k**2, n, k):
            number[j] = 0
        psum += k
        # k gives the actual prime numbers < n
print(psum)