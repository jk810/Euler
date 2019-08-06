#%% Project Euler Problem 4
# Justin Kim
# Largest palindrome made from the product of two 3-digit numbers

import time
start_time = time.time()

max = 0

#full_test = [0, 0, 0]
#for number1 in range(900,1000):        
#    for number2 in range(900,1000):
#        
#        product = number1*number2
#        product_string = str(product)
#        
#        for n in range(0,3):
#            if product_string[n] == product_string[len(product_string) - 1 - n]:
#                full_test[n] = 1
#            else:
#                full_test[n] = 0
#                
#        if full_test[0] == full_test[1] == full_test[2] == 1 and product > max:
#            max = product  
            
            
for a in range(900, 1000):
	for b in range(900, 1000):
		product = str(a*b)
		reverse = product[::-1]
		if (product == reverse) and (a*b > max):
			max = a*b
            
full_time = time.time() - start_time

print(max)

