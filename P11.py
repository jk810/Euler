import numpy as np

arr = np.loadtxt(r"\Users\JK31434\Desktop\Python docs\Project Euler\p11.txt", delimiter=" ")

dim = arr.shape[1]

prod = []
for k in range(20):
    for i in range(17):
        p = 1
        pp = 1
        for j in range(4):          # set of 4
            p *= arr[k, i + j]      # row sets
            pp *= arr[i + j, k]     # col sets
        prod.append(p)
        prod.append(pp)

for i in range(17):                 # row
    for j in range(17):             # column
        p = 1
        for k in range(4):
            p*= arr[i + k, j + k]
        prod.append(p)

for i in range(17):
    for j in range(3, 20):
        p = 1
        for k in range(4):
            p *= arr[i + k, j - k]
        prod.append(p)

print(max(prod))