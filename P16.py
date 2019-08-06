# Project Euler Problem 16
# Justin Kim
# Sum of the digits of 2**1000

import time
start_time = time.perf_counter()

n = 2**1000
# sum_digits = sum(list(map(int, str(n))))

sum_digits = sum(int(digit) for digit in str(n))


elapsed_time = time.perf_counter() - start_time

print(sum_digits)
