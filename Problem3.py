from math import sqrt

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n/i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))

###### http://stackoverflow.com/a/6800214 ######
#This will return all of the factors, very quickly, of a number n.
#
#Why square root as the upper limit?
#
#sqrt(x) * sqrt(x) = x. So if the two factors are the same, they're both the square root. If you make one factor bigger, you have to make the other factor smaller. This means that one of the two will always be less than or equal to sqrt(x), so you only have to search up to that point to find one of the two matching factors. You can then use x / fac1 to get fac2
#
#the reduce(list.__add__, ...) is taking the little lists of [fac1, fac2] and joining them together in one long list.
#
#The [i, n/i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0 returns a pair of factors if the remainder when you divide n by the smaller one is zero (it doesn't need to check the larger one too, it just gets that by dividing n by the smaller one.)
#
#The set(...) on the outside is getting rid of duplicates. I think this only happens for perfect squares. For n = 4, this will return 2 twice, so set gets rid of one of them.
#
#Edit: sqrt is actually faster than **0.5, but I'll leave it out as it's nice as a self-contained snippet.

number = 600851475143
factorsOfNum1 = sorted(list(factors(number)))
tempArray = sorted(list(factors(number)))

for factor in tempArray:
	if len(list(factors(factor))) > 2:
		factorsOfNum1.remove(factor)

print(factorsOfNum1[len(factorsOfNum1)-1])