
import os
import random
os.system('clear')


'''

Create a function that takes a number num and returns its length.
Examples

number_length(10) ➞ 2

number_length(5000) ➞ 4

number_length(0) ➞ 1
'''

def number_length(num):
	new_num = map(int, str(num))
	return len(list(new_num))

print(number_length(478551))