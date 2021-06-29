from sympy.ntheory import divisors

def is_ab(n):
    if sum(divisors(n)[:-1]) > n:
        return True
    else:
        return False

abs = [i for i in range(12, 28123) if is_ab(i)]
a_sums = set(i + j for i in abs for j in abs)
nums = set(range(28124))

print(sum(nums.difference(a_sums)))