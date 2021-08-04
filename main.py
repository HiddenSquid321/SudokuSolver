import numpy as np

grid = [[5,3,0,0,7,0,0,0,0], #Creates a Matrix to represent a grid
	 	[6,0,0,1,9,5,0,0,0],
	 	[0,9,8,0,0,0,0,6,0],
	 	[8,0,0,0,6,0,0,0,3],
	 	[4,0,0,8,0,3,0,0,1],
	 	[7,0,0,0,2,0,0,0,6],
	 	[0,6,0,0,0,0,2,8,0],
	 	[0,0,0,4,1,9,0,0,5],
	 	[0,0,0,0,8,0,0,7,9]]

print (np.matrix(grid))

def find_empty_box(grid): # Function to check for values in the matrix equal to 0
	for x in range(9):
		for y in range(9):
			if grid[x][y] == 0:
				return x, y 
			else:
				return 0