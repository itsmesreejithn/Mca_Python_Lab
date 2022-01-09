def sumOfThree(num1, num2, num3):
	if(num1 == num2 and num2 == num3 and num1 == num3):
		print("The three numbers are same therefore thrice their sum")
		sum = num1+num2+num3
		thriceSum = 3*sum
		return thriceSum
	else:
		sum = num1+num2+num3
		return sum

#Getting the numbers from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

#function call to find sum of three numbers
response = sumOfThree(num1, num2, num3)

#printing response
print("The  sum is ", response)

