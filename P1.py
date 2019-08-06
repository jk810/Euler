# Project Euler Problem 2
# Justin Kim
# Sum all natural numbers < 1000 that are multiples of 3 or 5

answer = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        answer += i

print(answer)

# sum([x for x in range(1,1001) if x % 3 ==0 or x % 5 ==0])
