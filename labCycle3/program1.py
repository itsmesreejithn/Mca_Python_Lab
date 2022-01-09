def simpleIntrest(p, a, t):
	if(a >= 60):
		r = 12
	else:
		r = 10
	
	print("The simple intrest amount is: ", (p*r*t)/100)


#simpel intrest calculation
name = input("Enter your name: ")

#Getting  the age from the user
age = int(input("Enter your age: "))

#Getting principal amount form the user
principalAmount = int(input("Enter the principal amount: "))

#Getting time duration for user
timeDuration = int(input("Enter the time duration: "))

#function call simple intrest
simpleIntrest(principalAmount, age, timeDuration)

