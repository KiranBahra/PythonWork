#while loops
a=5
while (a>0):
	print(a)
	# -= is a reverse incrementing 
	a-=1


quit = input('Type "enter" to quit:')
while quit!= "enter":
	quit= input ('Type "enter" to quit:')


while True:
	userCommand = input("Enter your command: ")
	if userCommand=="quit":
		break
	else:
		print ("You typed " + userCommand)


#start of rock paper scissors game

player1= input("Player one,choose:")
player2 = input("Player two, choose:")

while (player1=="rock"):
	if player2=="scissors":
		print (player1 +" beats " +player2)
		print ("Player one wins")
		break
	if player2== "paper":
		print (player2 +" beats " +player1)
		print ("Player two wins")


while (player1 =="scissors"):
	if player2=="rock":
		print (player2 +" beats " +player1)
		print("Player two wins")
		break
	if player2=="paper":
		print (player1 +" beats " +player2)
		print("Player one wins")

while (player1=="paper"):
	if player2=="rock":
		print (player1 +" beats " +player2)
		print("Player one wins")
		break

	if player2=="scissors":
		print (player2 +" beats " +player1)
		print("Player two wins")
