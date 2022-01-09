import math

def sumOfSeries(num):
	sum = 0
	for i in range (1, num+1):
		sum += i**i/math.factorial(i)
	return sum

#Getting limit form the user
n = int(input("Enter the limit upto which series is to be sumed: "))
print(sumOfSeries(n))

