def prime(n):
	result = []
	for x in range(1,n):
		count = 0
		for y in range(1,x):
			if x % y == 0:
				count += 1

		if count == 1:
			result.append(x)
	return result


	
n = int(input('Please enter the number: '))
print(prime(n))