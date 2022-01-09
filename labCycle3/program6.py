'''Adds the variable lengthe arguments and display sum'''
def addVariables(*args):
	sum = 0
	for num in args:
		sum += num
	print("Sum of variables")
	for num in args:
		print(num)
	print (" is ", sum)


#passing variable length arguments
addVariables(1, 2, 3, 4, 5, 6, 7, 19, 100)
