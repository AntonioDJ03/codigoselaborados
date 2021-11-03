from tkinter import *
#Generacion raiz principal de aplicacion
root = Tk()

menubar=Menu(root)
root.config(menu=menubar)

#Generando menus Archivo con sus submenus
menu_archivo=Menu(menubar, tearoff=0)
menu_archivo.add_command(label= "Nuevo")
menu_archivo.add_command(label="Abrir")
menu_archivo.add_command(label="Guardar")
menu_archivo.add_command(label="Cerrar")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

#Generando menu editar con sus subtemas
menu_editar=Menu(menubar, tearoff=0)
menu_editar.add_command(label="Copiar")
menu_editar.add_command(label="Cortar")
menu_editar.add_command(label="Pegar")


#Generando menu ayuda con sus subtemas
menu_help=Menu(menubar, tearoff=0)
menu_help.add_command(label="Acerca de")
menu_help.add_separator()
menu_help.add_command(label="Ayuda Online")

menubar.add_cascade(label="Archivo", menu=menu_archivo)
menubar.add_cascade(label="Editar", menu=menu_editar)
menubar.add_cascade(label="Ayuda", menu=menu_help)

#Creacion final de la aplicacion
root.mainloop()