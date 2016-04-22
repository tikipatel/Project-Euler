def performChain(n):
	numSteps = 0
	while n > 1:
		numSteps += 1
		if n % 2 == 0:
			n = n / 2
		else:
			n = (3 * n) + 1
	return numSteps+1


longestChain = 0
numberWithLongestChain = 0
for i in range(1,1000001):
	iChain = performChain(i)
	if longestChain < iChain:
		numberWithLongestChain = i
		longestChain = iChain
		
print((longestChain, numberWithLongestChain))