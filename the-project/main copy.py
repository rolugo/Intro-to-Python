# Rosendo Lugo Jr.
# The Project
# The game of Rock, Paper, Scissors against the computer.

# A random number is created for the computer choice.
import random


# Game option for the Rock, Paper and Scissors game.
game_options = ("rock", "paper", "scissors")
game_options_2 = ("y", "n")
continue_playing = True


while continue_playing:

    def main():
        winner()

    # User turn to choose one of the three options.
    def user_choice():
        player = None
        while player not in game_options:
            player = input('Enter your choice of "Rock", "Paper", or "Scissors": ').lower()
        return player

    # The computer chooses at random from the three predetermine game options.
    def computer_choice():
        computer = random.choice(game_options)
        print("The computer's selected:", computer)
        print('')
        return computer

    # Find the winner based on the user choice and computer choice
    def winner():
        champ = True
        while champ:
            player = user_choice()
            computer = computer_choice()
            if player == computer:
                print("It's a draw! Play until there is a Winner!")
            if player == "rock" and computer == "scissors":
                print("Rock smashes scissors. You WIN!")
                print("")
                break
            elif player == "scissors" and computer == "paper":
                print("Scissors cuts paper. You WIN!")
                print("")
                break
            elif player == "paper" and computer == "rock":
                print("Paper wraps rock. You WIN!")
                print("")
                break
            elif computer == "rock" and player == "scissors":
                print("Rock smashes scissors. The computer WINS!")
                print("")
                break
            elif computer == "scissors" and player == "paper":
                print("Scissors cuts paper. The computer WINS!")
                print("")
                break
            elif computer == "paper" and player == "rock":
                print("Paper wraps rock. The computer WINS! ")
                print("")
                break
        return champ


    # Call the main function
    main()
    play_again = None
    while play_again not in game_options_2:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if not play_again == "y":
            continue_playing = False
            print('Thank you for playing!')