fibs = [1, 1]

def nth_f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibs[n - 2] + fibs[n - 3]

i = 3
while len(str(fibs[-1])) < 1000:
    fibs.append(nth_f(i))
    i += 1
print(i - 1)