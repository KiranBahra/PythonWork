#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
varInput = input("Enter Text:")
#this reverses the text as a string is a list
varReverse=varInput[::-1]
print(varReverse)
if (varInput== varReverse):
 	print("This is a palindrome")
else:
 	print("This is not a palindrome")

#reversed is a set word in python that will reverse the string
for i in reversed(varInput):
	print(i)

