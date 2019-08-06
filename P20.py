# Project Euler Problem 20
# Justin Kim
# Sum of digits in 100!

import math

n = int(math.factorial(100))

sumDigits = sum(int(x) for x in str(n))

print(sumDigits)
