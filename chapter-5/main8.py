# Rosendo Lugo Jr.
# Chapter 5 Programming
# The game of Rock, Paper, Scissors against the computer.

# A random number is created for the computer choice.
import random

game_options = ("rock", "paper", "scissors")


def main():
    winner()


def user_choice():
    player = None
    while player not in game_options:
        player = input('Enter your choice of "Rock", "Paper", or "Scissors": ').lower()
    return player


def computer_choice():
    computer = random.choice(game_options)
    print("The computer's selected:", computer)
    print('')
    return computer


def winner():
    champ = True
    while champ:
        player = user_choice()
        computer = computer_choice()
        if player == computer:
            print("It's a draw! Play until there is a Winner!")
            break
        else:
            if player == "rock" and computer == "scissors":
                print("Rock smashes scissors. You WIN!")
            elif player == "scissors" and computer == "paper":
                print("Scissors cuts paper. You WIN!")
            elif player == "paper" and computer == "rock":
                print("Paper wraps rock. You WIN!")
            elif computer == "rock" and player == "scissors":
                print("Rock smashes scissors. The computer WINS!")
            elif computer == "scissors" and player == "paper":
                print("Scissors cuts paper. The computer WINS!")
            elif computer == "paper" and player == "rock":
                print("Paper wraps rock. The computer WINS! ")
        return champ

    print('Thanks for playing.')
# Call the main function
main()
