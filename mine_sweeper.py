# a comand line version of mind sweeper
import random

class Board:
	def __init__(dim, num_bombs):
		self.dim = dim
		self.num_bombs = num_bombs

		# create the board
		# using helper functions
		self.board = self.make_new_board() # where we're gonna plant the bombs as well 
		# assign values to each board location (cell) 
		# so the use would know whether to stop digging or keep going
		self.assign_values_to_board()
		# keep track of the places where the user's dug
		self.dug = set()

	def make_new_board(self):
		# construct a new board based on the dimensions and number of bombs
		# using list of lists 
		board = [[None for _ in range(self.dim)] for _ in range(self.dim)]

		# plant bombs 
		bombs_planted = 0
		while bombs_planted < self.num_bombs:
			# select a random location from the board 
			# replace its value which is None with a bomb string
			new_bomb_location = random.randint(0, self.dim**2 - 1)
			# get the row and the column of the random location
			row = new_bomb_location // self.dim
			column = new_bomb_location % self.dim


			# check what's in that random location 
			if board[row][column] == '*': # an * represents a bomb
				# then there is a bomb in this location so skip it
				continue

			board[row][column] = '*'
			bombs_planted += 1

		return board 

	def assign_values_to_board(self):
		# now that we have bombs planted we can assign value to each empty square 
		# from 0-8 where representing number of bombs around this square
		for row in range(self.dim):
			for column in range(self.dim):
				if self.board[row][column] == '*':
					continue
				else: 
					# call a function to check the number of neighboring bombs
					self.board[row][column] = self.get_num_neighboring_bombs(r, c) 


	def get_num_neighboring_bombs(self, row, column):
		# check the grid of 8 neighbors around this cell 
		num_neighboring_bombs = 0 
		# carefull not to get out of bounds
		# using min & max functions
		for r in range(max(0, row-1), min(self.dim-1, row+1)+1):
			for c in range(max(0, column-1), min(self.dim-1, column+1)+1):
				if r = row and c = column:
					# this is the original cell so pass it
					continue
				if self.board[r][c] == '*':
					# then we have a new neighboring bomb
					num_neighboring_bombs += 1

		return num_neighboring_bombs

	def dig(self, row, column):
		# dig at row & column
		self.dug.add((row, column))
		# return true if it's successfull other wise return 0 'gameover'
		if self.board[row][column] == '*':
			return False
		elif sefl.board[row][column] > 0:
			# that cell has neighboring bombs so just return true
			return True

		# otherwise self.board[row][column] must = 0
		# using the same logic from get_num_neighboring_bombs function to check it's neighbors
		# and dig recursively
		for r in range(max(0, row-1), min(self.dim-1, row+1)+1):
			for c in range(max(0, column-1), min(self.dim-1, column+1)+1):
				# check if this cell has benn dug before
				if (r, c) in self.dug:
					continue
				self.dig(r, c)

		return True

	def __str__(self):
		# a magic function that shows the user the board after each new process
		# goole why do we need magic functions in python ?
		# why not a normal function just like the rest ?


def play(dim=10, num_bombs=10):
	# step 1 create the board and plant the bombs
	board = Board(dim, num_bombs)
	# step 2 show the user the board and ask them where they wanna dig 
	# step 3 if there's a bomb in that location 
	# we show the game over else keep digging automatically until
	# you reach a location next to the bomb
	# step 4 repeast steps 2 and 3 until there's no more clean
	# (non bomb) location to dig then it's victory
	pass