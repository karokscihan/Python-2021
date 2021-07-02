
import os
import random
os.system('clear')


'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


'''

user = int(input("Please enter a number to find fibonacci numbers: "))

def findFib(a):
	fib = []
	total = 0
	fib.append(0)
	fib.append(1)

	for each in range(2,a+1):
		total = fib[each - 2] + fib[each -1]
		fib.append(total)
	print(fib)
findFib(user)






