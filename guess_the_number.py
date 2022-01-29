import random 

def guess(upper_range):
	# generate the random number
	random_number = random.randint(1, upper_range)

	# init guess
	guess = 0

	# getting the user's guess
	while guess != random_number:
		guess = int(input(f'Guess a number between 1 and {upper_range}: '))
		
		# giving the user some clues
		if guess > random_number: 
			print('Sorry guess again, aim lower')
		elif guess < random_number:
			print('Sorry guess again, aim higher')

	print(f'WOW you got it right, you guessed the right number {random_number}')


def computer_guess():
	lowest_number = int(input('Enter your lowest number.. '))
	highest_number = int(input('Enter your highest number.. '))
	feedback = ''


	while feedback != 'c':
		if lowest_number != highest_number:
			guessed_number = random.randint(lowest_number, highest_number)
		else: 
			guess = lowest_number

		feedback = input(f'Is {guessed_number} correct Enter \
			your feddback C for correct H for \
			guess higher and L for guess lower ')

		if feedback == 'H':
			lowest_number += 1
		else:
			highest_number -= 1

	print(f'WOW I guessed your number {guessed_number} correctly')

computer_guess()

