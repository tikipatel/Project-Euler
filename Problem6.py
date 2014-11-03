def sumOfSquares(min, max):
	sum = 0
	for i in range(min, max+1):
		sum += i**2
	return sum

def squareOfSums(min, max):
	sum = 0
	for i in range(min, max + 1):
		sum += i
	return sum**2

print(squareOfSums(1,100) - sumOfSquares(1,100))
