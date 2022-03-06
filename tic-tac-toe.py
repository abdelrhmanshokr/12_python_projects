from player.py import HumanPlayer, RandomComputerPlayer 

class TicTacToe:
	def __init__(self):
		# defining the game board as a 3*3 matrix
		# it's gonna be represented as a single array
		self.board = [' ' for _ in range(9)]
		self.current_winner = None

	def print_board(self):
		# getting rows as a group of 3s 
		for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
			print('| ' + ' | '.join(row) + ' |')

	# using static method when it's not gonna access any proprty 
	# of the class itself
 	# so there is no need to pass self to this function 
	@staticmethod
	def print_board_numbers():
		number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
		for row in number_board:
			print('| ' + ' | '.join(row) + ' |')

	def available_moves(self):
		return [i for i, spot in enumerate(self.board) if spot == ' ']
		# the same code as the following
		# moves = [] 
		# for(i, spot) in enumerate(self.board):
		# 	if spot == ' ':
		# 		moves.append(i)
		# return moves

	def empty_squares(self):
		return ' ' in self.board

	def num_empty_squares(self):
		return self.board.count(' ')

	def make_move(self, letter, square): 
		# check if the move is valid 
		if self.board[square] == ' ':
			# then make the move and return true
			self.board[square] = letter
			# check if this letter won 
			# then assign its letter as the current winner
			if self.check_winner(square, letter):
				self.current_winner = letter
			return True
		return False

	def check_winner(self, square, letter):
		# if 3 squares have the same letter in a row then
		# we have a winner 
		# first check the rows 
		row_index = square // 3 # divide by three and round down
		row = self.board[row_index * 3 : (row_index + 1) * 3]
		# if all letters in this row are the same and equal the input letter
		# this that letter won ! 
		if all([spot == letter for spot in row]):
			return True

		# if not then check columns
		column_index = square % 3
		column = [self.board[column_index + i * 3] for i in range(3)]
		if all([spot == letter for spot in column]):
			return True

		# finally check the diagonal 
		if square % 2 == 0:
			# top left to buttom right diagonal
			diagonal1 = [self.board[i] for i in [0, 4, 8]]
			# check if this diagonal is a winner
			if all([spot == letter for spot in diagonal1]):
				return True

			# top right to buttom left diagonal
			diagonal2 = [self.board[i] for i in [2, 4, 6]]
			# check if this diagonal is a winner
			if all([spot == letter for spot in diagonal2]):
				return True

		# finally if all these checks fail then we don't have a 
		# winner yet
		return False 

def play(game, x_player, o_player, print_game=True):
	if print_game:
		game.print_board_numbers()

	starting_letter = 'x'
	# while there are empty spaces then the game goes on
	while game.empty_squares():
		# get the next move to the right player 
		if letter == 'x':
			square = x_player.get_move(game)
		else:
			square = o_player.get_move(game)

		# now it's time to make a move to make it count
		# assigning a letter to an empty square
		if game.make_move(letter, square):
			if print_game:
				print f'{letter} makes a move to {square}'
				game.print_board()
				print('')

			# here we need to check if there is a winner 
			if current_winner:
				print f'{letter} WINS!'

			# after making a move we need to alternate letters 
			letter = 'o' if letter = 'x' else 'x'

		print('It\'s a tie')


if __name__ == '__main__':
	x_player = HumanPlayer('x')
	o_player = RandomComputerPlayer('o')
	game = TicTacToe()
	play(game, x_player, y_player, print_game=True)