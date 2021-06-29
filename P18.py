dat = open(r"\Users\JK31434\Desktop\Python docs\Project Euler\p18.txt", 'r')
tri = [[int(i) for i in line.split()] for line in dat]

for i in range(13, -1, -1):     # start at second to bottom row
    b = len(tri[i])
    for j in range(b):
        if tri[i][j] + tri[i + 1][j] > tri[i][j] + tri[i + 1][j + 1]:
            tri[i][j] += tri[i + 1][j]
        else:
            tri[i][j] += tri[i + 1][j + 1]
print(tri)