#%% Project Euler Problem 6
# Justin Kim
# Difference between the square of the sum and the sum of the squares

def problem6(n):
    sumsq = 0
    sqsum = 0
    for i in range(n + 1):
        sumsq += i**2
        sqsum += i
    sqsum *= sqsum
    ans = sqsum - sumsq
    return ans

ans = problem6(100)