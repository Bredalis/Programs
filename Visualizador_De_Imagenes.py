
# Programa creado para visualizar
# cualquier imagen a partir de la url

def visualizador(url):

	import tkinter as tk
	from PIL import Image, ImageTk

	interfaz = tk.Tk()
	interfaz.resizable(0, 0)
	interfaz.title("Imagenes")

	icono = "Imagen.ico"
	interfaz.iconbitmap(icono)
	
	foto = Image.open(url)
	img = ImageTk.PhotoImage(foto)

	fondo = tk.Label(interfaz, image = img)
	fondo.pack()

	interfaz.mainloop()