import math 
import random 

class Player:
	def __init__(self, letter):
		# letter is x or o 
		self.letter = letter

	# a function so every player could get their next move given a game
	def get_next_move(self, game):
		# pass as this is the base player class 
		# each case will have its own get_next_move implementation
		pass 


# using inheritance to build a human player and a computer 
# player on top of that Player class 
class RandomComputerPlayer(Player):
	def __init__(self, letter):
		# using the super() to refer to the initializaiton of 
		# the Player class passing the letter along with it
		super().__init__(letter)

	def get_next_move(self, game):
		# for the computer player it's gonna choose 
		# randomly from available moves 
		square = random.choice(game.available_moves()) 

		return square

class HumanPlayer(Player):
	def __init__(self, letter):
		super().__init__(letter)

	def get_next_move(self, game):
		# first get a valid input from the user
		valid_input = False
		val = None
		while not valid_input:
			square = input(self.letter + '\'s turn. Input move from 0 to 8: ')
			# apply checks to see if the user's input is valid or not 
			try:
				val = int(square)
				if val not in game.available_moves():
					raise ValueError
				# else 
				valid_input = True
			except ValueError:
				print('Invalid square try again !')

		return val

class SuperComputerPlayer(Player):
	def __init__(self, letter):
		super().__init__(letter)

	def minimax(self, game, letter):
		# the game here is like a screenshot of the state of the game at that point
		max_player = self.letter # the super computer player
		other_player = 'o' if letter == 'x' else 'x'

		# first we need to check if the previous move is a winner
		# so we need to define the base cases 
		if game.check_winner == other_player:
			# for the minimax algorithm we need to keep track of the score 
			# and the state as well 
			return {
				'position': None,
				'score': 1 * (game.empty_squares() + 1) if other_player == max_player else -1 * (game.empty_squares() + 1)
			}
		elif not game.empty_squares():
			# no winner 
			return {
				'position': None, # because we didn't move
				'score': 0 
			}

		# now into the algorithm itself 
		if letter == max_player:
			# if the player is yourself
			best = {
				'position': None,
				'score': - math.inf # we initialize the score to - inf so we have to increase it in every iteration
			}
		else:
			# it's the other player
			best = {
				'position': None,
				'score': math.inf # we initialized the score to inf so we have to decrease it in every iteration 
			}

		# check all available moves then choose the best one
		for possible_move in game.available_moves():
			# step 1 make a move, try that spot
			game.make_move(letter, possible_move) 
			# step 2 recurse using minimax to simulate that move
			simulated_score = self.minimax(game, other_player) 
			# step 3 undo that move to check other positions 
			game.board[possible_move] = ' '
			game.current_winner = None
			simulated_score['position'] = possible_move
			# step 4 update the dictionaries if needed 
			if letter == max_player:
				simulated_score['score'] > best['score']
				best = simulated_score
			else: 
				# the player is the min player the other player 
				if simulated_score['score'] < best['score']:
					best = simulated_score

		return best

	def get_next_move(self, game):
		# this is where the super computer player is gonna choose the best square
		if len(game.available_moves()) == 9:
			square = random.choice(game.available_moves()) # random choice
		else:
			# get the best square to win based on the minimax algorithm 
			square = self.minimax(game, self.letter)['position']

		return square