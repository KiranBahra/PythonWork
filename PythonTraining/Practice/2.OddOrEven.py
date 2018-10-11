#Ask the user for a number. 
#Depending on whether the number is even or odd, print out an appropriate message to the user. 
#Hint: how does an even / odd number react differently when divided by 2?

varinp = input ("Please enter a number:")
varinp =int(varinp)

#finding the modulus, if the value is 0 it is fully divisible by 2, hence it is even. if the value is 1 it is odd
varDiv = varinp % 2 
#print(str(varDiv))

if int(varDiv) ==0:
	print("The number you entered, "+ str(varinp) + " is Even")
else:
	print("The number you entered, "+ str(varinp) + " is Odd")


