#####
#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old
#####
name= input("Please enter your name:")
age= input("Please enter your age:")

#calculation

#100 minus the age 
#add the difference to the current year
#convert age to integer
age =int(age)

print ("your name is " + name)
diff = 100-age
#print(diff)

yr100 = 2017 + diff
print ("the year " +name + " will be 100 is " + str(yr100))
