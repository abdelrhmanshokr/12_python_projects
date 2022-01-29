import random 

def is_win(player, opponent):
	# returns true if the player wins 
	if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
		or (player == 'p' and opponent == 'r'):
		return True


def play():
	user_input = input('Enter p for paper, r for rock and s for sissors what\'s your choice?!\n')

	random_choice = random.choice(['p', 'r', 's'])

	if user_input == random_choice:
		return f'it\'s a tie we both chose {random_choice}'

	if is_win(user_input, random_choice):
		return f'You win I chose {random_choice}'
	
	return f'I win I chose {random_choice}'


print(play())