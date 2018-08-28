# CS 61A Spring
# exam_prep01 
# http://inst.eecs.berkeley.edu/~cs61a/sp18/assets/pdfs/exam_prep01.pdf

# CODE WITH PROBLEMS
# 1. You Complete Me
def longest_increasing_suffix(n):
	m,suffix, k= 10, 0, 1
	while n:
		last, n = n % 10, n // 10
		if last > n % 10:
			suffix ,k = suffix + last * k, k * 10
		else: 
			return suffix
	return suffix

# 2. A Highly Intelligent Animal
def sandwich(n):
	tens, ones = n//10, n%10
	n = n // 100
	while n:
		if ones == n%10:
			return True
		else: 
			tens, ones  = tens % 10, n*10+tens
			n = sandwich(ones)
	return False

# 3. Digit Fidget
def luhn_sum(n):
	def luhn_digit(digit):
		x = digit * 2
		return (x//10) + (x%10)
	total, odd = 0, 0
	while n:
		odd = n % 10
		n = n // 10
		last = n % 10
		total = total+odd + luhn_digit(last)
		n = n//10
	return total
	
# WHAT WOULD PYTHON PRINT?
# 1. Dog Goes Woof
"""
Expression                 Evaluates to      Interactive output
add(square(2), mul(3,4))        16                4, 12
print(print(print(2)))          None            2,None, None
cat(3,4)                        9                  4,9
square(cat(5)                   Error             Error
cat(square(2), print(5))         16              5, None, 16
cat(print(square(3)), 8)        Error              9, Error
"""

# ENVIRONMENT DIAGROMS
# 1. Supernatural
'''
f1: joker [parent = f1]
		superman     abs
		abs(-2)      2
		ivy          1
		return       nanana(batman)

f2: nanana [parent = f2]
		batman       abs
		batman       batman(joker)         
		return       3

f3: batman [parent = f2]
		joker        -2
		retrun       -3
'''

# 2. Envy, Iron, Mint
'''
f1: peace [parent = f1]
		today       joy
		harmony     5
		love+1      4
		return      7
		
f2: joy [parent = f1]
		peace       4
		peace       6
		love        5
		return      2
'''
