from tkinter import Tk, Label


def magic(event):
    label.config(text=event.keysym)


window = Tk()
window.bind("<Key>", magic)

label = Label(window, font=("Helvetica",100))
label.pack()

window.mainloop()

