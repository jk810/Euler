a = range(999, 100, -1)
b = []

for i in a:
    for j in a:
        n = str(i*j)
        if n == n[::-1]:
            b.append(int(n))
print(max(b))
