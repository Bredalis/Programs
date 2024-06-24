
# Librerias

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

contenido = open("Manual.txt", "r").read()
exec(contenido)
manual("Manual_Abrir_Imagen.txt")

ventana = tk.Tk()
ventana.title("Imagen")
ventana.resizable(0, 0)
ventana.iconbitmap("Camara_2.ico")

foto = ""
ventana_fondo = tk.Label(ventana)
ventana_fondo.pack()

# Cerrar la ventana 

class Cerrar:
    def __init__(self, herencia):

        self.x = tk.Toplevel(herencia)
        self.x.title("Salir")
        self.x.geometry("90x70")

        self.herencia = herencia
        
        tk.Label(self.x, text = "Abre una imagen").pack(pady = 5)

        tk.Button(self.x, text = "Si", 
            activebackground = "skyblue", command = self.agregar_imagen).place(x = 30, y = 30)

        tk.Button(self.x, text = "No", 
            activebackground = "skyblue", command = self.salir).place(x = 60, y = 30)

    def agregar_imagen(self):

        global foto

        try:

            folder = filedialog.askopenfilename(title = "Open", initialdir = "C:", 
                filetypes = (("Icon", "*.png"), ("Icon", "*.ico"), ("Icon", "*.jpg")))

            img = Image.open(folder)
            foto = ImageTk.PhotoImage(img)

            ventana_fondo.config(image = foto)

        except Exception as e: 
            print(f"Error {e}")
 
    def salir(self):

        self.x.destroy()
        self.herencia.destroy()

clase = Cerrar(ventana)
ventana.mainloop()