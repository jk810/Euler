with open(r"\Users\JK31434\Desktop\Python docs\Project Euler\p22_names.txt") as f:
    names = sorted(f.read().replace('"', '').split(','))
f.closed

ts = 0
alph = 'abcdefghijklmnopqrstuvwxyz'
alphnum ={}
for i, l in enumerate(alph):
    alphnum[l] = i + 1

for i, n in enumerate(names):
    s = 0
    for j in n:
        s += alphnum[j.lower()]
    ts += (i + 1)*s

print(ts)