import numpy as np
import time

start_time = time.time()

grid = [[0,0,0,0,0,1,2,0,0], # Initializes a multidemnsional array to represent the sudoku grid 
	[0,0,0,0,0,0,3,4,0],
	[0,0,0,0,0,0,0,5,6],
	[0,0,0,0,0,0,0,0,7],
	[0,0,0,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,0,0],
	[7,2,0,0,0,0,0,0,0],
	[0,4,8,0,0,0,0,0,0],
	[0,0,6,3,0,0,0,0,0]]

print (np.matrix(grid))

# Function to Check for Empty Boxes
def find_empty_box(sudoku):
	for x in range(9): # Ranged for loop 
		for y in range(9):
			if sudoku[x][y] == 0: # Checks for boxes equal to zero which represents an empty box
				return x, y 
	
	return None, None # This for if there are no empyt boxes in the puzzles

# Function to check the numbers in each box are valid
def Answer_Valid(sudoku, guess, row, col): 
	row_values = sudoku[row]    
	if guess in row_values: # Checks against row values if the condition is true it returns false because it isnt valid
		return False

	column_values = [sudoku[i][col]for i in range(9)] 
	if guess in column_values: # If the conditon is true it returns false because the column values arent valid
		return False

	row_start = (row // 3) * 3 # This checks the squares
	col_start = (col // 3) * 3
	
	# for loops and if statements to check if the box is valid
	for x in range(row_start, row_start + 3): 
		for y in range(col_start, col_start + 3):
			if sudoku[x][y] == guess:
				return False

		return True

#Function to solve using a backtracking method
def Solver(sudoku):
	row, col = find_empty_box(sudoku) # This uses the function find_empty_box to locate where a guess can be made
	
	# if there is nowhere left on the grid it returns true
	if row is None:
		return True
	
	# Inputs a number between 1 and 9 where valid
	for guess in range(1,10):
		# Uses the function answer valid to check the guess was valid
		if Answer_Valid(sudoku, guess, row, col):
			sudoku[row][col] = guess # If the answer was valid it puts it in the relevant place on the grid
			# Uses recursion to call the solver function
			if Solver(sudoku):
				return True
		# If something becomes invalid it uses backtracking to test a new number(s)
		sudoku[row][col] = 0
	# Returns false if the puzzles is not solvable
	return False

# Prints the solved puzzle
print(Solver(grid))

print(np.matrix(grid))

print("%s seconds " % (time.time() - start_time))
