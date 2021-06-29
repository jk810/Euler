spiral_nums = [1]

for i in range(2, 1001, 2):
    a = spiral_nums[-1]
    for j in range(1, 5):
        spiral_nums.append(i*j + a)

print(sum(spiral_nums))