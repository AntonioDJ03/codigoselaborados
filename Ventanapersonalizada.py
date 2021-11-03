import tkinter as tk

def abrir():
    window2 = tk.Toplevel(window)
    window2.config(bg="green")
    window2.geometry("220x300") #ancho, alto
    window2.title("Ventana2")

window = tk.Tk()
window.config(bg="yellow")
window.geometry("220x150")
window.title("Ventana1")
button = tk.Button(window,text="Abrir Ventana2", command=abrir)
button.grid(row=1, column=1)
window.mainloop()