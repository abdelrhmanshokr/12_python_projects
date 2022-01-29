import random 

def guess(x):
	# generate the random number
	random_number = random.randint(1, x)

	# init guess
	guess = 0

	# getting the user's guess
	while guess != random_number:
		guess = int(input(f'Guess a number between 1 and {x}: '))
		
		# giving the user some clues
		if guess > random_number: 
			print('Sorry guess again, aim lower')
		elif guess < random_number:
			print('Sorry guess again, aim higher')

	print(f'WOW you got it right, you guessed the right number {random_number}')

guess(10)
