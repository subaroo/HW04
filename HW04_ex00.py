#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports

import random

# Body

def create_random():
	computer_num = random.randint(1, 25)
	return computer_num



def get_user_num():	
	user_number = raw_input("Please guess a number between 1 and 25: ")
	try:
		user_guess = int(user_number)
	except: 
		print("Try again by giving me a number.")
		return get_user_num()		
	else:
		return user_guess


def test_numbers():
	computer_num = create_random()
	guesses = 1
	while guesses < 6:
		user_guess = get_user_num()
		if user_guess == computer_num:
			print("Great job you got the number right.")
			break
		else:
			if user_guess < computer_num:
				print("Your number is too low.")
			else:
				print("Your number was too high")	
		guesses = guesses + 1



################################################################################
def main():
	test_numbers()
    

if __name__ == '__main__':
    main()