import random
cont = 1

def opp():
	opp_hand = randint(1,3)
	return opp_hand

def you():
	count = 0
	good = ["rock", "paper", "scissors"]
	while count == 0:
		you_hand = input("Rock, Paper, or Scissors?").lower()
		if you_hand not in good:
			print("That was not a valid submission.")
		count += 1
		return good.index(you_hand) + 1

def check():
	if opp() == you():
		print("Tie!")
	elif opp() > you():
		print("You lose!")
	print("You win!")

def replay():
	count2 = 0
	while count2 == 0:
		rep = input("Play again? (y/n)")
		if rep.lower == "n":
			cont -= 1
			count2 += 1
		elif rep.lower == "y":
			cont += 0
			count2 += 1
		else:
			print("Not valid.")


def playgame():
	if cont == 1:
		






