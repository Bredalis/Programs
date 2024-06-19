
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

foto = ""

contenido = open("Manual.txt", "r").read()
exec(contenido)

def abrir_imagen():

    ventana = tk.Tk()
    ventana.title("Imagen")
    ventana.resizable(0,0)
    ventana.iconbitmap("Camara_2.ico")

    global foto

    try:

        folder = filedialog.askopenfilename(title = "Open", initialdir = "C:", 
            filetypes = (("Icon", "*.png"), ("Icon", "*.ico"), ("Icon", "*.jpg")))

        img = Image.open(folder)
        foto = ImageTk.PhotoImage(img)

        etiqueta = tk.Label(ventana, image = foto)
        etiqueta.pack()

        class Cerrar:

            def __init__(self, herencia):

                self.x = tk.Toplevel(herencia)
                self.x.title("salir")

                self.herencia = herencia
                
                tk.Label(self.x, text = "¿Quieres abrir otra?").grid(row = 0, column = 0, columnspan = 2)

                self.si = tk.Button(self.x, text = "Si", activebackground = "skyblue", command = self.salir)
                self.si.grid(row = 1, column = 0, padx = 5, pady = 5)

                self.no = tk.Button(self.x, text = "No", activebackground = "skyblue", command = self.minimizar)        
                self.no.grid(row = 1, column = 1, padx = 5, pady = 5)

            def salir(self):

                global foto

                try:

                    folder = filedialog.askopenfilename(title = "Open", initialdir = "C:", 
                        filetypes = (("Icon", "*.png"), ("Icon", "*.ico"), ("Icon", "*.jpg")))

                    img = Image.open(folder)

                    foto = ImageTk.PhotoImage(img)

                    etiqueta.config(image = foto)

                except AttributeError:
                    print("Ha ocurrido un error")         

            def minimizar(self):

                self.x.destroy()
                self.herencia.destroy()

        class Registro:

            def __init__(self, herencia):

                self.herencia = herencia
                self.herencia.protocol("WM_DELETE_WINDOW", self.al_cerrar)

            def al_cerrar(self):
                clase = Cerrar(ventana)
                self.herencia.wait_window(clase.x)

        if __name__ == "__main__":
            clase = Registro(ventana)

    except Exception: 
        print("Ocurrio un error")

    ventana.mainloop()

manual("Manual_Abrir_Imagen.txt")
abrir_imagen()