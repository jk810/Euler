d = 2
for n in range(2, 1000000):
    c = [n]
    a = c[-1]
    while a != 1:
        if a % 2 == 0:
            a /= 2
            c.append(a)
        else:
            a = 3*a + 1
            c.append(a)
    if len(c) > d:
        d = len(c)
        print(n)