
import os
import random
os.system('clear')


'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message
 of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

'''
def new_game():
	player1 = str(input('Player 1, Please select "Rock", "Paper" or "Scissors": '))
	player2 = str(input('Player 2, Please select "Rock", "Paper" or "Scissors": '))
	player1 = player1.title()
	player2 = player2.title()
	print("Player 1 is selected: " + str(player1) + "\n")
	print("Player 2 is selected: " + str(player2) + "\n")
	return game(player1, player2)


def game(a,b):
	if a == "Rock":
		if b == "Rock":
			print("Tie")
		elif b == "Paper":
			print("Player 2 Won")
		else:
			print("Player 1 Won")
	if a == "Paper":
		if b == "Paper":
			print("Tie")
		elif b == "Scissors":
			print("Player 2 Won")
		else:
			print("Player 1 Won")
	if a == "Scissors":
		if b == "Scissors":
			print("Tie")
		elif b == "Rock":
			print("Player 2 Won")
		else:
			print("Player 1 Won")
	end()


def end():			
	while True:
		selection = str(input("Do you want to play new game? Y or N :"))
		selection = selection.upper()
		if selection == "N":
			print("Thank you for playing")
			break
		else:
			new_game()

new_game()







