x = 0
for i in range(1,1000):
	if i % 15 == 0:
		x += i
	elif i % 3 == 0:
		x += i
	elif i % 5 == 0:
		x += i
print(x)
