import random
import string
from hangman_words import words

def get_valid_word(words):
	word = random.choice(words)
	while '-' in word or ' ' in word:
		get_valid_word(words)

	return word

def play_hangman(words):
	word = get_valid_word(words) 
	word_letters = set(word) # letters in the word
	alphabet = set(string.ascii_uppercase) # all alphabet letters
	used_letters = set() #what the user guessed
	lives = 6  

	while len(word_letters) > 0 and lives > 0:
		# letting the user know what words they used 
		print('You have ', lives, ' remaining, And You have used these letters', ' '.join(used_letters))

		# showing the word with -s in place of letters they haven't guessed yet
		word_list = [letter if letter in used_letters else '-' for letter in word]
		print('Current word', ' '.join(word_list))

		# getting user's input
		user_input = input('Type something: ').upper()
		if user_input in alphabet - used_letters:
			used_letters.add(user_input)
			if user_input in word_letters:
				word_letters.remove(user_input)
			else:
				lives -= 1 
				print(f'Your letter {user_input} is not in the word, You have {lives} lives remaining')
		elif user_input in used_letters:
			print('You\'v already choosen this letter')
		else:
			print('You entered an invalid letter, try again')

	if lives > 0:
		# gets here when they're done guessing the word
		print(f'You have guessed it right: {word}')
	else: 
		print(f'You have lost, the word was {word}, wanna play again ?')

play_hangman(words)