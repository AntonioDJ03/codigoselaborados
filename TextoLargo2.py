from tkinter import *
root = Tk()

texto = Text(root)
texto.pack()
texto.config(width=50, height=5, font=("Montserrat Black",12), padx=25, pady=15, selectbackground="purple")

root.mainloop()