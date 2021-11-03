from tkinter import *
#Creando la raiz
root = Tk()
imagen=PhotoImage(file="C:/Users/anton/OneDrive/Documentos/TERCER SEMESTRE/TOPICOS AVANZADOS DE PROGRAMACIÓN/Codigos/balon.gif")
Label(root, image=imagen, bd=0).pack()

#Craer loop final
root.mainloop()