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

comp_list = list(range(1,101))
comp_selection = random.choice(comp_list)
count = 0
def game(num, a = 1, b = 100):
    global count
    print("I have chosen " + str(num) + "\nShould I go Higher or Lower or Correct? ")
    user = input("Your Selection: ")
    if user == "L":
        count = count + 1
        low_game(a, num)
    elif user == "H":
        count = count + 1
        high_game(num, b)
    else:
        print("I have guessed correctly in " + str(count) + " tries")


def low_game(old_low, new_High):
   
    x = new_High
    new_comp_list = list(range(old_low, x))
    new_comp_selection = random.choice(new_comp_list)	
    game(new_comp_selection, old_low, x)


def high_game(new_low, old_high):
    
    x = new_low + 1
    new_comp_list = list(range(x, old_high))
    new_comp_selection = random.choice(new_comp_list)	
    game(new_comp_selection,x, old_high)

game(comp_selection)
