#Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]

#need to check each list, if it contains repeats 
# for each item in a we check for each item in b and if they are the same
# add to another list and print


for aItem in a:
	for bItem in b:
		if aItem == bItem:
			
			c.append(aItem)



print(c)

# can do it two ways 

for aEl in a:
	if aEl in b:
		c.append(aEl)
print(c)