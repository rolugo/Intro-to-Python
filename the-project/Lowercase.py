from tkinter import *

root = Tk()
root.geometry('250x250')
root.title("Meta' Translator")
root.configure(background="#35424a")

# Entry widget object
textin = StringVar()


# press ENTER key to activate translate button
def return_pressed(event):
    clk()
    return event


def clk():
    entered = ent.get().lower()
    output.delete(0.0, END)
    try:
        textin = exlist[entered]
    except ValueError:
        textin = 'Word not found'
    output.insert(0.0, textin)


# heading
lab0 = Label(root, text='Translate English Words to Meta\'', bg="#35424a", fg="silver", font='none 11 bold')
lab0.place(x=0, y=2)

# Entry field
ent = Entry(root, width=15, font='Times 18', textvariable=textin, bg='white')
ent.place(x=30, y=30)

# focus on entry widget
ent.focus()

# Search button
but = Button(root, padx=1, pady=1, text='Translate', command=clk, bg='powder blue', font='none 18 bold')
but.place(x=60, y=90)

# press ENTER key to activate Translate button
root.bind('<Return>', return_pressed)

# output field
output = Text(root, width=15, height=1, font='Times 18', fg="black")
output.place(x=30, y=170)

# prevent sizing of window
root.resizable(False, False)

# Dictionary
exlist = {
    "hat": "ɨ̀də̀m",
    "hoe": "əsɔ́",
    "honey": "jú",
    "chest": "ɨgɔ̂",
    "eye": "ɨghə́",
    "ear": "ǝ̀tǒŋ",
}

root.mainloop()
