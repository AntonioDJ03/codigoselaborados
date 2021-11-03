from tkinter import *
#Configuración de la ventana raiz
root = Tk()

label = Label(root, text="Hola Mundo soy Antonio")
label.pack()
Label(root, text="Otra Etiqueta - #2").pack(anchor="ne")
Label(root, text="Esta es la Etiqueta - #3").pack(anchor = "sw")

label.config(bg="green",fg="blue",font=("Arial",20))
#Bucle final
root.mainloop()