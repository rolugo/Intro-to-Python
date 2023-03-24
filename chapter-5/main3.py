# Rosendo Lugo Jr.
# Chapter 5 Programming
# The game of Rock, Paper, Scissors against the computer.

# A random number is created for the computer choice.
import random


def main():
    player_wins()
    computer_wins()


player = input('Enter your choice of "Rock", "Paper", or "Scissors": ').lower()
print(player)
computer = random.choice(["Rock", "Paper", "Scissors"]).lower()
print("The computer's selected:", computer)
print('')


def player_wins():
    if player == "rock" and computer == "scissors":
        print("You WIN! Rock smashes scissors.")
    elif player == "scissors" and computer == "paper":
        print("You WIN! Scissors cuts paper.")
    elif player == "paper" and computer == "rock":
        print("You WIN! Paper wraps rock.")


def computer_wins():
    if computer == "rock" and player == "scissors":
        print("The computer WINS! Rock smashes scissors.")
    elif computer == "scissors" and player == "paper":
        print("The computer WINS! Scissors cuts paper.")
    elif computer == "paper" and player == "rock":
        print("The computer WINS! Paper wraps rock.")


while player == computer:
    print("It's a draw! Start the game again.")
    player = input('Enter a new choice of "Rock", "Paper", or "Scissors": ').lower()


# Call the main function
main()