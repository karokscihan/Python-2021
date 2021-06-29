
import os
os.system('clear')

'''

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

'''




	
bank = {"Deposit": 0, "Withdraw": 0, "Total": 0}

def deposit():
	depo = int(input("Please enter the amount you would like to deposit: "))
	bank["Deposit"] += depo

def withdraw():
	with_draw = int(input("Please enter the amount you would like to withdraw: "))
	bank["Withdraw"] -= with_draw
def total():
	bank["Total"] = bank["Deposit"] + bank["Withdraw"]

while True:
	try:
		select = int(input(''' 
			Please select transaction: 
			1 - Deposit
			2 - Withdraw
			3 - Show Total
			4 - Exit \n'''))

		if select == 4: 
			break

		elif select == 3:
			total()
			print("Total Money: ", bank["Total"])
			continue

		elif select == 2:
			withdraw()
			continue

		elif select == 1:
			deposit()
			continue
			
		elif select < 1 or select > 4:
			raise ValueError
		break
	except ValueError:
		print("Incorrect Selection, Please try again")	

	