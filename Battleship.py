import random

#SETUP!!!
#-------------------------
#Prints out grid
grid = []

for i in range(5):
	grid.append(["O"] * 5)

for p in grid:
	print("".join(grid))

# Chooses row for battleship
row = random.randint(0,4)
#Chooses column for battleship
col = random.randint(0,4)

#debug
print(row)
print(col)

#to check if hit
#set equal to number of spaces to hit
check = 1

#Play!!!!!
#--------------------------

while check != 0:  #if all ships aren't sunk
	
	#check if valid coordinates
	bad = 0  
	r_options = ["0", "1", "2", "3", "4"] 
	print() 
	r_select = input("Row(0-4):")
	if r_select in r_options:
		print("yes") #debug
		r_valid = int(r_select)
	else:
		bad += 1

	c_options = ["0", "1", "2", "3", "4"]
	c_select = input("Column(0-4):")
	if c_select in c_options:
		print("yes") #debug
		c_valid = int(c_select)
	else:
		bad += 1
	print()
	if bad > 0:
		print("Enter valid numbers.")
	print()

	if r_valid == row and c_valid == col:
		print("yes") #debug
		grid[r_valid][c_valid] = "D"
		print("Congrats!")
		



	#GRID REPRING!!!
	#-------------------
	#Prints out grid
	for i in range(5):
		print(grid)





