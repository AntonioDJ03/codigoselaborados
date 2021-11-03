from tkinter import *
#Configuración de la ventana raiz
root = Tk()

label = Label(root, text="Hola Mundo soy Antonio")
label.pack()
label = Label(root, text="Otra Etiqueta - #2").pack(anchor = "ne")
label = Label(root, text="Esta es la Etiqueta - #3").pack(anchor = "sw")
label.config(bg="blue")

#Bucle final
root.mainloop()