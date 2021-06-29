# Project Euler Problem 19
# Justin Kim
# Counting Sundays

import time
import numpy as np
start = time.perf_counter()

calendar = np.array([])

jan = np.arange(1,32)
feb = np.arange(1,29)
leapfeb = np.arange(1,30)
mar = np.arange(1,32)
apr = np.arange(1,31)
may = np.arange(1,32)
jun = np.arange(1,31)
jul = np.arange(1,32)
aug = np.arange(1,32)
sep = np.arange(1,31)
octo = np.arange(1,32)
nov = np.arange(1,31)
dec = np.arange(1,32)

for i in range(0, 101):
    if i == 0:
        calendar = np.hstack((jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec))
    elif i % 4 == 0:
        calendar = np.hstack((calendar, jan, leapfeb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec))
    else:
        calendar = np.hstack((calendar, jan,feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec))

count = 0
for i in range(370,36891,7):
    if calendar[i] == 1:
        count += 1




import datetime
sundays = 0
for y in range(1901,2001):
	for m in range (1,13):
		d = datetime.date(y,m,1)
		if d.weekday() == 6: sundays += 1

# from datatime import date
# sum(date(y, m, 1).weekday() == 6 for y in range(1901, 2001) for m in range(1, 13))
print(sundays)
elapsed = time.perf_counter() - start
