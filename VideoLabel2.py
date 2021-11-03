from tkinter import *
root= Tk()
#StringVar son variables dinamicas que se deben craer despues del root
texto = StringVar()
texto.set("Un nuevo texto por StringVar")

label = Label(root, text="Otra Etiqueta")
label.config(bg="green",fg="blue", font=("Arial",20))
label.config(textvariable=texto)
label.pack()

#Bucle final
root.mainloop()