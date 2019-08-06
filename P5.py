#%% Project Euler Problem 5
# Justin Kim
# Smallest positive number that is evenly divisible by numbers 1-20

import time
start_time = time.time()

a = 4849845         # product of all primes between 1-20
test = [0] * 20
trigger = False

while trigger == False:
    for j in range(1, 21):
        if a % j == 0:
            test[j - 1] = 1
            if all(m == 1 for m in test):
                trigger = True
        else:
            test[j-1] = 0
            a += 4849845
            break   # restart for loop while maintaining value of a

elapsed = time.time() - start_time

