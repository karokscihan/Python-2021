
'''
This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)
'''

import os
import random
os.system('clear')

user = int(input("Please enter a number between 1-100: "))
print("Your Number is: " + str(user))

Low = 1
High = 100

comp_list = list(range(1,101))
comp_selection = random.choice(comp_list)

def game(num):
	print("I have chosen " + str(num) + " Should I go Higher or Lower or Correct? ")
	user = input()

	if user == "L":
		low_game(num, High)
	elif user == "H":
		high_game(num, Low)
	else:
		print("I have guessed correctly")


def low_game(num_low, low_new):

	new_comp_list = list(range(low_new, num_low))
	new_comp_selection = random.choice(new_comp_list)	
	game(new_comp_selection)


def high_game(num_high, high_new):
	new_comp_list = list(range(num_high, High_new))
	new_comp_selection = random.choice(new_comp_list)	
	game(new_comp_selection)

game(comp_selection)







