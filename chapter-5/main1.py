# Rosendo Lugo Jr.
# Chapter 5 Programming
# The game of Rock, Paper, Scissors against the computer.

# A random number is created for the computer choice.
import random

# Constants for the Rock, Paper, Scissors game.
rock = 1
paper = 2
scissors = 3

user_choice = input('Enter your choice of "Rock", "Paper", or "Scissors": ')
print(user_choice)
print("The computer's selection: ")


# The main function.
def main():
    # Call the random function.
    random_rps() # rps = rock, paper, and scissors
    # Call the random function.
    draw()


def random_rps():
    if random.randint(rock, paper) == rock:
        print('rock')
    elif random.randint(rock, paper) == paper:
        print('paper')
    else:
        print('scissors')


def draw():
    if user_choice == rock or user_choice == paper or user_choice == scissors:
        return print('Both players made the same choice.\n'
                     'The game must be played again to determine the winner.')


# Call the main function
main()
