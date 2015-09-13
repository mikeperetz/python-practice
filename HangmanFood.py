import random

#def play():

#	replay = input("Play again (y/n)?")
#	if replay == "y":
#		play = 1
#	elif replay == "n":
#		play = 0
#	else: 

def make_word():
	foods = ["apple", "banana", "pear", "orange", "chicken", "gravy", "squash", "cabbage", "pumpkin", "broccoli", "cucumber", "spinach", "mushroom", "popsicle", "steak", "meatballs", "strawberries", "watermelon", "juice", "water", "syrup", "sausage", "peanuts"]
	word = foods[random.randint(0,len(foods))]
	#print(word) #debug
	return word

def check(word, guess):
	if guess in word:
		#print("yes") #debug
		return True
	return False
	
def find_ind(word, guess):
	ind = []
	for i in range(len(word)):
		if word[i] == guess:
			ind.append(i)
	#print(ind) #debug
	return(ind)

def valid_guess(guess):
	letters = [a,b,c,d,e,f,g,h,i,jk,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

def play_game():
	word = make_word()
	board = "_ "*len(word)
	lst_board = list(board)
	count = 0
	win = 0
	wrongs = []
	while count != 3:
		if "_" in board:
			print(board)
			print()
			print("Guesses left: %d" % (3-count))
			print("Already guessed:" + " " + ", ".join(wrongs))
			print()
			guess = input("Guess a letter:").strip().lower()
			#print(guess) #debug
			if check(word, guess):
				indx = find_ind(word, guess)
				if len(indx) >= 1:
					lst_board[indx[0]*2]  = word[indx[0]]
				if len(indx) >= 2:
					lst_board[indx[1]*2]  = word[indx[1]]
				if len(indx) >= 3:
					lst_board[indx[2]*2]  = word[indx[2]]
				board = ("".join(lst_board))
			else:
				wrongs.append(guess)
				print()
				print("----------------------")
				print()
				print("Nope!")
				count += 1
		else:
			win += 1
			count = 3
	if win > 0:
		print()
		print("You win!")
	else:
		print()
		print("You lose! The word was %s!" % word)

		print("")



	

play_game()
