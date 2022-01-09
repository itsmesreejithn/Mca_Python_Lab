#Method compare
def compare(string1, string2, n):
	#setString1 = set(string1)
	#setString2 = set(string2)
	for i in range(n):
		if(string1[i] == string2[i]):
			return True
		return False

#Getting two strings for user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

#Getting n terms to compare
n = int(input("Enter the n term to compare two string: "))

print(compare(str1, str2, n))
