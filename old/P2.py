#%% Project Euler Problem 2
# Justin Kim
# Sum even fibonacci numbers that are < 4,000,000

a = 1
b = 2
count = 0

while b <= 4000000:
    if b % 2 == 0:
        count += b
    elif a % 2 ==0:
        count += a
    a += b
    b += a

print(count)