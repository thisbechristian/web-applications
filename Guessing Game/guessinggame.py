# Define a function to retrieve the answer.
def get_answer(guess):

  # Initialize answer
  answer = ''

  # We only want to accept one of these values.
  while not answer in ['correct', 'higher', 'lower']:
    answer = raw_input("Is your age " + str(guess) + "? Enter correct, higher, or lower:\n")

    # Convert the value to lower case.
    answer = answer.lower()

  return answer

def guess():
	
	# Initialize bounds and guess variables
	lower = 0
	upper = 125
	guess = (upper+lower)/2
	
	# Propose the first guess to start the sequence of guesses
	answer = get_answer(guess)
	
	# Keep guessing until correct
	while (answer != 'correct'):
		
		if(answer == 'higher'):
			lower = guess
			guess = (upper+lower)/2
			answer = get_answer(guess)
			
		elif(answer == 'lower'):
			upper = guess
			guess = (upper+lower)/2
			answer = get_answer(guess)


print 'Welcome to guessing game!'
guess()
