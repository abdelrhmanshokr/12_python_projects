def find_next_empty(puzzle):
	for row in range(9):
		for col in range(9):
			if puzzle[row][col] == -1: # which means an empty space
				return row, col

	return None, None

def is_valid(puzzle, guess, row, col):
	# first check the row
	row_values = puzzle[row]
	if guess in row_values:
		return False

	# then check the column
	col_values = [puzzle[i][col] for i in range(9)]
	if guess in col_values:
		return False

	# finally check the little 3*3 square the guess is in
	row_start = (row // 3) * 3
	col_start = (col // 3) * 3
	for r in range(row_start, row_start + 3):
		for c in range(col_start, col_start + 3):
			if puzzle[r][c] == guess:
				return False 

	# if we reached this point then the guess is valid
	return True

def solve_sudoku(puzzle):
	# we're gonna solve sudoku using backtracking method
	
	# first step to choose somewhere to take the first guess
	row, col = find_next_empty(puzzle)

	# if row and column are None this means we're done
	if row is None and col is None:
		return True

	# else if there's an empty space take a guess between 1 and 9
	for guess in range(1, 10):
		# here check if it's a valid guess
		print(f"guess is {guess}") 
		print("-----------------")
		if is_valid(puzzle, guess, row, col):
			puzzle[row][col] = guess

			# finally recursively call the same function
			# to keep guessing the rest of empty places
			if solve_sudoku(puzzle):
				return True

		# but another case is if this guess isn't valid 
		# then we need to backtrack it (reset all mutated values)
		# and start all over again with a new guess
		puzzle[row][col] = -1 

	# finally if we tried every possible compination and it doesn't
	# work then it can't be solved
	return False

if __name__ == "__main__":
	example_board = [
		[3, 9, -1,  -1, 5, -1,  -1, -1, -1],
		[-1, -1, -1,  2, -1, -1,  -1, -1, 5],
		[-1, -1, -1,  7, 1, 9,  -1, 8, -1],

		[-1, 5, -1,  -1, 6, 8,  -1, -1, -1],
		[2, -1, 6,  -1, -1, 3,  -1, -1, -1],
		[-1, -1, -1,  -1, -1, -1,  -1, -1, 4],

		[5, -1, -1,  -1, -1, -1,  -1, -1, -1],
		[6, 7, -1,  1, -1, 5,  -1, 4, -1],
		[1, 1, 9,  -1, -1, -1, 2, -1, -1]
	]

	print(solve_sudoku(example_board))
	print(example_board)


