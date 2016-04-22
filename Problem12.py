from functools import reduce
from math import sqrt

def factors(n):    
	return set(reduce(list.__add__,([i, n/i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))

def triangularNumber(n):
	return sum(range(1,n+1))
	
print(len(factors(12375)))

print(triangularNumber(12376))

print(factors(76576500))
#	
#divisors = 0
#i = 1
#while divisors < 500:
#	tNumber = triangularNumber(i)
#	numDivisors = len(factors(tNumber))
#	divisors = numDivisors
#	print([tNumber," has ",numDivisors, " divisors"])
#	i += 1
#print(i)
