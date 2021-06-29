def sum_divisors(n):
    c = 0
    for i in range(1,n//2 + 1):
        if n % i == 0:
            c += i
    return c

amic = []
for a in range(1, 10000):
    b = sum_divisors(a)
    if a == sum_divisors(b) and a != b:
        if a not in amic:
         amic.append(a)

print(amic)
print(sum(amic))