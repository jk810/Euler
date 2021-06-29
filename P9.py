ar = range(1, 333)
br = range(2, 500)
cr = range(335, 997)

t = False
for i in ar:
    for j in br:
        for k in cr:
            if i + j + k == 1000 and i**2 + j**2 == k**2:
                t = True
                a = i
                b = j
                c = k
print(a*b*c)