# Project Euler Problem 17
# Justin Kim
# How many letters in spelling out numbers 1-1000
# SHORT LIBRARY WAY: NUM2WORD OR INFLECT

import time
start_time = time.perf_counter()


by_one = ["one", "two", "three", "four", "five", "six", "seven", "eight",
          "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
          "sixteen", "seventeen", "eighteen", "nineteen"]

by_ten = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
          "ninety"]

def spell_number(n):
    if n <= 19:
        return by_one[n - 1]
    elif 20 <= n <= 99:
        if n % 10 == 0:
            return by_ten[int(str(n)[0]) - 2]
        else:
            return by_ten[int(str(n)[0]) - 2] + "-" + by_one[int(str(n)[1]) - 1]
    elif 100 <= n <= 999:
        if str(n)[1] == "0" and str(n)[2] == "0":
            return by_one[int(str(n)[0]) - 1] + " hundred"
        elif str(n)[1] == "0":
            return by_one[int(str(n)[0]) - 1] + " hundred and " + by_one[int(str(n)[2]) - 1]
        elif str(n)[2] == "0" and str(n)[1] == "1":
            return by_one[int(str(n)[0]) - 1] + " hundred and " + by_one[9]
        elif str(n)[2] == "0":
            return by_one[int(str(n)[0]) - 1] + " hundred and " + by_ten[int(str(n)[1]) - 2]
        elif str(n)[1] == "1":
            return by_one[int(str(n)[0]) - 1] + " hundred and "+ by_one[int(str(n)[2]) + 9]
        else:
            return by_one[int(str(n)[0]) - 1] + " hundred and " + by_ten[int(str(n)[1]) - 2] + "-" + by_one[int(str(n)[2]) - 1]
    elif n == 1000:
        return "one thousand"

spelled = []
ans = 0
for i in range(1, 1001):
    spelled.append(spell_number(i))
    ans += sum(c != ' ' for c in spelled[i - 1])
    ans -= sum(c == '-' for c in spelled[i - 1])

elapsed_time = time.perf_counter() - start_time

print(ans)
asdf = 30
