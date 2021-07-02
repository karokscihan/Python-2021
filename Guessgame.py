
import os
import random
os.system('clear')


'''
This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)
'''



user = int(input("Please enter a number between 1-100: "))
print("Your Number is: " + str(user))

comp_list = list(range(1,101))
comp_selection = random.choice(comp_list)


def game(a, num, game_list):
			
	print("My guess is " + str(num))
	print("Should I go (L)ower, (H)igher or did I guessed correctly: ")
	user_answer = input()
	user_answer.upper()
	count = a + 1
	if user_answer == "Y":
		print("I guessed Correctly in " + str(count) + " guesses")
	elif user_answer == "L":
		low(count, num, game_list)
	else:
		high(count, num, game_list)


def low(counter, low_number, lst_low):
	try:
		new_selection = random.choice(lst_low[:low_number-1])
		return game(counter, new_selection, lst_low)
	except IndexError:
		print("No more guesses")

def high(counter, high_number, lst_high):
	try:
		new_selection = random.choice(lst_high[high_number:])
		return game(counter, new_selection, lst_high)
	except IndexError:
		print("No more guesses")

game(0, comp_selection, comp_list)


'''		
		new_high_list = lst_high[0+high_number:]
		print("list high: " + str(new_high_list))
	'''









