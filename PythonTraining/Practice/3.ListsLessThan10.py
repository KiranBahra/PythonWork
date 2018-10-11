##write a program that prints out all the elements of the list that are less than the number that has been inputted
a= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[] 
varIn = input("Enter a random number:")
for item in a:
	if item < int(varIn):
		print(item)
		b.append(item)

print(b)
