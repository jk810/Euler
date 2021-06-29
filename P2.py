a = [1, 2]
while max(a) < 4000000:
    a.append(sum(a[-2:]))

ans = sum([i for i in a if i%2 == 0])
print(ans)