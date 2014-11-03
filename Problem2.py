#import numpy
#def F(n):
#    if n == 0: return 0
#    elif n == 1: return 1
#    else: return F(n-1)+F(n-2)
#
#fibArray = []
#
#for i in range(0,34):
#	x = F(i)
##	print(x)
#	if x % 2 == 0:
#		fibArray.append(x)


firstNum = 2
secondNum = 1 + firstNum
thirdNum = 0

sum = firstNum

while secondNum < 4000000:
	thirdNum = firstNum + secondNum
	firstNum = secondNum
	secondNum = thirdNum
	if thirdNum %2 == 0:
		sum += thirdNum

print(sum)
#print(fibArray)
#print(sum(fibArray))