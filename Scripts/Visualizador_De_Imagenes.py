
# Visualizar imagen a partir de la url

def visualizador(url):
	import tkinter as tk
	from PIL import Image, ImageTk

	ventana = tk.Tk()
	ventana.resizable(0, 0)
	ventana.title("Imagenes")
	ventana.iconbitmap("../IMG/Imagen.ico")
	
	foto = Image.open(url)
	img = ImageTk.PhotoImage(foto)

	fondo = tk.Label(ventana, image = img)
	fondo.pack()

	ventana.mainloop()