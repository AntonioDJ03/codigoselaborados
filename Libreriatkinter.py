import tkinter as tk  #importando y renombrando la libreria
window = tk.Tk() #Creando pantalla principal
window.geometry("200x150") #Configurando características de la ventana principal
button=tk.Button(window,text="Testing") #Agregando un botón de prueba
button.grid(row=5,column=5)
window.mainloop() #Loop final

