#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

varInp= input("Please enter a number:")
varInp =int(varInp)

#have a list, the limit of the list is the user input
listRange = list(range(1,varInp+1))
divisorList = []

for number in listRange:
	if varInp % number ==0:
		divisorList.append(number)

print(divisorList)