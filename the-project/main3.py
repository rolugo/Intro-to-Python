# Rosendo Lugo Jr.
# The Project
# The game of Rock, Paper, Scissors against the computer.

# import tkinter
# A random number is created for the computer choice.
from tkinter import *
import random

# Game option for the Rock, Paper and Scissors game.
game_options = ("Rock", "Paper", "Scissors")
game_options_2 = ("y", "n")
continue_playing = True


def main():

    # Initialize Window
    root = Tk()
    root.geometry('450x450')
    root.title('Rock, Paper, Scissors - Project')
    root.config(bg='seashell3')

    # Heading
    Label(root, text='Rock, Paper, Scissors', font='arial 20 bold', bg='seashell2').pack()

    # User turn to choose one of the three options.
    player_entry = StringVar()
    Label(root, text='Enter your selection: Rock, Paper, Scissors', font='arial 15 bold', bg='seashell2').place(x=10, y=60)
    Entry(root, font='arial 15', textvariable=player_entry, bg='antiquewhite2').place(x=90, y=110)

    def computer_choice():
        # The computer chooses at random from the three predetermine game options.
        computer = random.choice(game_options)
        Label(root, text=f'The computer selected: {computer}', font='arial 15 bold', bg='seashell2').place(x=10, y=220)
        return computer

    # Function to play
    result = StringVar()

    # Find the winner based on the user choice and computer choice
    def play():
        computer = computer_choice()
        player = player_entry.get()
        if player.lower() == computer.lower():
            result.set("It's a draw! Play until there is a Winner!")
        elif player.lower() == "rock" and computer.lower() == "scissors":
            result.set("Rock smashes scissors. You WIN!")
        elif player.lower() == "scissors" and computer.lower() == "paper":
            result.set("Scissors cuts paper. You WIN!")
        elif player.lower() == "paper" and computer.lower() == "rock":
            result.set("Paper wraps rock. You WIN!")
        elif computer.lower() == "rock" and player.lower() == "scissors":
            result.set("Rock smashes scissors. The computer WINS!")
        elif computer.lower() == "scissors" and player.lower() == "paper":
            result.set("Scissors cuts paper. The computer WINS!")
        elif computer.lower() == "paper" and player.lower() == "rock":
            result.set("Paper wraps rock. The computer WINS! ")
        else:
            result.set("Error: enter rock, paper, or scissors")

    # Reset
    def reset():
        result.set("")
        player_entry.set("")

    # Exit
    def exit():
        root.destroy()

    # Button
    Entry(root, font='arial 10 bold', textvariable=result, bg='antiquewhite2', width=50).place(x=10, y=280)
    Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play).place(x=150, y=150)
    Button(root, font='arial 13 bold', text='PLAY AGAIN', padx=5, bg='seashell4', command=reset).place(x=70, y=340)
    Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=exit).place(x=230, y=340)
    root.mainloop()


# Call the main function
main()
