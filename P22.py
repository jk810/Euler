# Project Euler Problem 22
# Justin Kim
# Name scores

import time
start = time.perf_counter()

f = open('p022_names.txt')

names = sorted(f.read().replace('"', '').split(','))

alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
            'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
            'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
            'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

digit_names = []

for i in range(len(names)):
    temp = 0
    for j in names[i]:
        temp += alphabet[j]
    digit_names.append(temp)
    digit_names[i] *= (i + 1)

ans = sum(x for x in digit_names)

elapsed = time.perf_counter() - start

print(ans)
print(names)
