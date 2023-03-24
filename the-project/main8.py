# Rosendo Lugo Jr.
# The Project
# The game of Rock, Paper, Scissors against the computer.

# import tkinter
# A random number is created for the computer choice.
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random

# Game option for the Rock, Paper and Scissors game.
game_options = ("Rock", "Paper", "Scissors")


def main():
    # Initialize the main window
    root = Tk()
    root.geometry('450x450')
    root.title('Rock, Paper, Scissors - Project')
    root.config(bg='seashell3')

    # Heading
    Label(root, text='Rock, Paper, Scissors', font='arial 20 bold', bg='seashell2').pack()

    # User turn to choose one of the three options.
    player_entry = StringVar()
    Label(root, text='Enter your selection: Rock, Paper, Scissors', font='arial 15 bold', bg='seashell2')\
        .place(x=10, y=60)

    def computer_choice():
        # The computer chooses at random from the three predetermine game options.
        computer = random.choice(game_options)
        var = StringVar()
        var.set(f'The computer selected: {computer}')
        computer_label.config(textvariable=var)
        return computer

    # Function to play
    result = StringVar()

    # Find the winner based on the user choice and computer choice
    def play(event):
        computer = computer_choice()
        player = player_entry.get()
        if player.lower() == computer.lower():
            tk.messagebox.showinfo("Winner!", "It's a draw! Play until there is a Winner!")
        elif player.lower() == "rock" and computer.lower() == "scissors":
            tk.messagebox.showinfo("Winner!", "Rock smashes scissors. You WIN!")
        elif player.lower() == "scissors" and computer.lower() == "paper":
            tk.messagebox.showinfo("Winner!", "Scissors cuts paper. You WIN!")
        elif player.lower() == "paper" and computer.lower() == "rock":
            tk.messagebox.showinfo("Winner!", "Paper wraps rock. You WIN!")
        elif computer.lower() == "rock" and player.lower() == "scissors":
            tk.messagebox.showinfo("Winner!", "Rock smashes scissors. The computer WINS!")
        elif computer.lower() == "scissors" and player.lower() == "paper":
            tk.messagebox.showinfo("Winner!", "Scissors cuts paper. The computer WINS!")
        elif computer.lower() == "paper" and player.lower() == "rock":
            tk.messagebox.showinfo("Winner!", "Paper wraps rock. The computer WINS! ")
        else:
            tk.messagebox.showinfo("Warning!", "Error: enter rock, paper, or scissors")

    # Play again
    def play_again():
        result.set("")
        player_entry.set("")
        var = StringVar(root)
        var.set("")
        computer_label.config(textvariable=var)

    # Exit
    def exit_fun():
        root.destroy()

    computer_label = Label(root, text='', font='arial 15 bold', bg='seashell2')
    computer_label.place(x=10, y=220)

    # This binds the player's entry to the enter key in the keyboard.
    play_entry = Entry(root, font='arial 15', textvariable=player_entry, bg='antiquewhite2')
    play_entry.bind("<Return>", (lambda event: play(play_entry.get())))
    play_entry.place(x=90, y=110)

    # This displays the results of the winners.


    # The reset and exit buttons.
    play_button = Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4',
                         command=(lambda: play(play_entry.get())))
    play_button.place(x=150, y=150)
    Button(root, font='arial 13 bold', text='PLAY AGAIN', padx=5, bg='seashell4', command=play_again).place(x=70, y=360)
    Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=exit_fun).place(x=230, y=360)
    root.mainloop()


# Call the main function
if __name__ == '__main__':
    main()
