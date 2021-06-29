numlist = open(r"\Users\JK31434\Desktop\Python docs\Project Euler\p13.txt", 'r')
nums = numlist.read().splitlines()

nums = [int(i) for i in nums]

S = sum(nums)
print(str(S)[:10])