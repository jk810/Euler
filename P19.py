d_in_m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date_list = []

for i in range(1900, 2001):
    if i % 4 == 0 and i != 1900:
        d_in_m[1] = 29
    else:
        d_in_m[1] = 28
    for j in d_in_m:
        for k in range(j):
            date_list.append(k + 1)

index_1st = [i for i, d in enumerate(date_list) if d == 1 and i > 365]

c = 0
for i in index_1st:
    if i % 7 == 6:
         c += 1

print(c)