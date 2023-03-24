# Rosendo Lugo Jr.
# Chapter 5 Programming
# The game of Rock, Paper, Scissors against the computer.

# A random number is created for the computer choice.
import random

game_options = ("rock", "paper", "scissors")
continue_playing = True


while continue_playing:

    def main():
        winner()

    player = None
    computer = random.choice(game_options)

    while player not in game_options:
        player = input('Enter your choice of "Rock", "Paper", or "Scissors": ').lower()

    print("The computer's selected:", computer)
    print('')


    def winner():
        if player == computer:
            print("It's a draw! Start the game again.")
        elif player == "rock" and computer == "scissors":
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


    # Call the main function
    main()
