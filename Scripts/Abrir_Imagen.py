
# Librerías
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

<<<<<<< HEAD
manual_contenido = open("../TXT/Manual.txt", "r").read()
exec(manual_contenido)
=======
contenido = open("../TXT/Manual.txt", "r").read()
exec(contenido)
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
manual("../TXT/Manual_Abrir_Imagen.txt")

ventana = tk.Tk()
ventana.title("Imagen")
ventana.resizable(0, 0)
<<<<<<< HEAD
ventana.iconbitmap("../IMG/Camara.ico")
=======
ventana.iconbitmap("../IMG/Camara_2.ico")
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da

foto = ""
ventana_fondo = tk.Label(ventana)
ventana_fondo.pack()

<<<<<<< HEAD
class CerrarVentana:
    def __init__(self, herencia):
        self.x = tk.Toplevel(herencia)
        self.x.title("Salir")
        self.x.geometry("90x70")
        self.herencia = herencia
        
        tk.Label(self.x, text = "Abre una imagen").pack(pady = 5)
        tk.Button(self.x, text = "Si", activebackground = "skyblue", 
            command = self.agregar_imagen).place(x = 30, y = 30)

        tk.Button(self.x, text = "No", activebackground = "skyblue", 
            command = self.salir_ventana).place(x = 60, y = 30)

    def agregar_imagen(self):
=======
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

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
        global foto

        try:
            folder = filedialog.askopenfilename(title = "Open", initialdir = "C:", 
                filetypes = (("Icon", "*.png"), ("Icon", "*.ico"), ("Icon", "*.jpg")))

            img = Image.open(folder)
            foto = ImageTk.PhotoImage(img)
<<<<<<< HEAD
            ventana_fondo.config(image = foto)

        except Exception as e: 
            print(f"Error inesperado: {e}")
 
    def salir_ventana(self):
        self.x.destroy()
        self.herencia.destroy()

clase_ventana = CerrarVentana(ventana)
=======

            ventana_fondo.config(image = foto)

        except Exception as e: 
            print(f"Error {e}")
 
    def salir(self):

        self.x.destroy()
        self.herencia.destroy()

clase = Cerrar(ventana)
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
ventana.mainloop()