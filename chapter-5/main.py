# Rosendo Lugo Jr.
# Chapter 5 Programming
# The game of Rock, Paper, Scissors against the computer.

# A random number is created for the computer choice.
import random

# Constants for the Rock, Paper, Scissors game.
rock = 1
paper = 2
scissors = 3

# The main function.
def main():
    # The pick variable
    pick = 0

    while pick != draw:
        # display the instructions
        instructions()

        if random.randint(rock, paper) == rock:
            print('Rock')
        elif random.randint(rock, paper) == paper:
            print('Paper')
        else:
            print('Scissors')


def winner():
    if user_choice == rock or user_choice == paper or user_choice == scissors:
        print('Both players made the same choice.\n'
              'The game must be played again to determine the winner.')
        return instructions()


def instructions():
    user_choice = input('Enter your choice of "Rock", "Paper", or "Scissors": ')
    print(user_choice)
    print("The computer's selection: ")

# Call the main function
main()

