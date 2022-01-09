#check even or odd

#Method to check for even or odd
def evenOdd(number):
	if(number % 2 == 0):
		return 1
	else:
		return -1


#Getting number for the user to check
num = int(input("Enter a number to check for even or odd: "))

#function call to check for even or odd
response = evenOdd(num)

#checking response to detemine
if(response == 1):
	print("The given number ", num, " is even")
else:
	print("The given number ", num, "is odd") 
