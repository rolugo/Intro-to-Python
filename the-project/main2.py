# Rosendo Lugo Jr.
# The Project
# The game of Rock, Paper, Scissors against the computer.

# A random number is created for the computer choice.
from tkinter import *
import random

# Game option for the Rock, Paper and Scissors game.
game_options = ("rock", "paper", "scissors")
game_options_2 = ("y", "n")
continue_playing = True

while continue_playing:

    def main():
        play()

    # Initialize Window
    root = Tk()
    root.geometry('400x400')
    root.title('Rock, Paper, Scissors - Project')
    root.config(bg='seashell3')

    # Heading
    Label(root, text='Rock, Paper, Scissors', font='arial 20 bold', bg='seashell2').pack()

    # User turn to choose one of the three options.


    def user_choice():
        player = StringVar()
        while player not in game_options:
            Label(root, text='Enter one choice: Rock, Paper, Scissors', font='arial 15 bold',
                  bg='seashell2').place(x=10, y=70)
            Entry(root, font='arial 15', textvariable=player, bg='antiquewhite2').place(x=90, y=130)
        return player

    # The computer chooses at random from the three predetermine game options.
    def computer_choice():
        computer = random.choice(game_options)
        print("The computer's selected:", computer)
        print('')
        return computer

    result = StringVar()

    # Find the winner based on the user choice and computer choice
    def play():
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

    # Reset
    def reset():
        result.set("")
        return reset

    # Exit
    def exit_fun():
        root.destroy()
        return exit_fun

    # Button
    Entry(root, font='arial 10 bold', textvariable=result, bg='antiquewhite2', width=50, ).place(x=25, y=250)
    Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play).place(x=150, y=190)
    Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command=reset).place(x=70, y=310)
    Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=exit_fun).place(x=230, y=310)
    root.mainloop()

    # Call the main function
    main()
    play_again = None
    while play_again not in game_options_2:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if not play_again == "y":
            continue_playing = False
            print('Thank you for playing!')