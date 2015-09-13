from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row) #debug
print(ship_col)

ship_row2 = random_row(board)
ship_col2 = random_col(board)
print(ship_row2) #debug
print(ship_col2)

ship_row3 = random_row(board)
ship_col3 = random_col(board)
print(ship_row3) #debug
print(ship_col3)


check = 1 #set to how many spaces
turn = 0 #astehtics

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
while check != 0: #check if lost

    #PLAYER!!!
    #---------------------

    print()
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print()
        print("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = "@"
        check -= 1
        if check == 0:
            print("You Win!")
            print_board(board) 
            break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print()
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print()
            print("You guessed that one already.")
        else:
            print()
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

    #OPPONENT!!!
    #----------------------
    opp_guess_row = random_row(board)
    opp_guess_col = random_col(board)

    while(board[opp_guess_row][opp_guess_col] == "X") or (board[opp_guess_row][opp_guess_col] == "@"):
        opp_guess_row = random_row(board)
        opp_guess_column = random_col(board)

            
    if opp_guess_row == ship_row and guess_col == ship_col:
        print()
        print("Sorry! You lost!")
        check -= 1
    else:
        board[opp_guess_row][opp_guess_col] = "X"
    # Print (turn + 1) here!
        turn += 1
        print()
        print("Turn", turn)
        print_board(board) 
