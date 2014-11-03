from math import sqrt

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n/i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))

number = 600851475143
factorsOfNum1 = sorted(list(factors(number)))
tempArray = sorted(list(factors(number)))

for factor in tempArray:
	if len(list(factors(factor))) > 2:
		factorsOfNum1.remove(factor)

print(factorsOfNum1[len(factorsOfNum1)-1])