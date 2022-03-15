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