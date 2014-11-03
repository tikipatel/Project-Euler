#def div20(n):
#	x = []
#	for i in range(1,10):
#		x.append(n % i)
#	if sum(x) > 0:
#		return False
#	else:
#		return True
#		
#for i in range(1,5, 5000):
#	if (div20(i)):
#		print(i)

#x = range(1,21,1)
#print(x)
i = 20;
while (i %  2 != 0 or i %  3 != 0 or i %  4 != 0 or i %  5 != 0 or
         i %  6 != 0 or i %  7 != 0 or i %  8 != 0 or i %  9 != 0 or
         i % 10 != 0 or i % 11 != 0 or i % 12 != 0 or i % 13 != 0 or
         i % 14 != 0 or i % 15 != 0 or i % 16 != 0 or i % 17 != 0 or
         i % 18 != 0 or i % 19 != 0 or i % 20 != 0):
    i += 20;
print(i)