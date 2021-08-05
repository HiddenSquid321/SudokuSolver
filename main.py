import numpy as np
if __name__=='__main__':
	grid = [[5,3,0,0,7,0,0,0,0], 
	 		[6,0,0,1,9,5,0,0,0],
	 		[0,9,8,0,0,0,0,6,0],
	 		[8,0,0,0,6,0,0,0,3],
	 		[4,0,0,8,0,3,0,0,1],
	 		[7,0,0,0,2,0,0,0,6],
	 		[0,6,0,0,0,0,2,8,0],
	 		[0,0,0,4,1,9,0,0,5],
	 		[0,0,0,0,8,0,0,7,9]]

print (np.matrix(grid))

def find_empty_box(puzzle): 
	for x in range(9):
		for y in range(9):
			if puzzle[x][y] == 0:
				return x, y 
	
	return None, None

def Answer_Valid(puzzle, guess, row, col): 
	row_values = puzzle[row]    
	if guess in row_values:
		return False

	column_values = [puzzle[i][col]for i in range(9)]
	if guess in column_values:
		return False

	row_start = (row // 3) * 3
	col_start = (col // 3) * 3

	for x in range(row_start, row_start + 3):
		for y in range(col_start, col_start + 3):
			if puzzle[x][y] == guess:
				return False

		return True

def Solver(puzzle):
	row, col = find_empty_box(puzzle)

	if row is None:
		return True

	for guess in range(1,10):
		if Answer_Valid(puzzle, guess, row, col):
			puzzle[row][col] = guess

			if Solver(puzzle):
				return True

		puzzle[row][col] = 0

	return False

print(Solver(grid))

print(np.matrix(grid))