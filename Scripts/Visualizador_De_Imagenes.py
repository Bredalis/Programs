
<<<<<<< HEAD
# Visualizar imagen a partir de la url

def visualizador(url):
	import tkinter as tk
	from PIL import Image, ImageTk

	ventana = tk.Tk()
	ventana.resizable(0, 0)
	ventana.title("Imagenes")
	ventana.iconbitmap("../IMG/Imagen.ico")
=======
# Programa creado para visualizar
# cualquier imagen a partir de la url

def visualizador(url):

	import tkinter as tk
	from PIL import Image, ImageTk

	interfaz = tk.Tk()
	interfaz.resizable(0, 0)
	interfaz.title("Imagenes")
	interfaz.iconbitmap("../IMG/Imagen.ico")
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
	
	foto = Image.open(url)
	img = ImageTk.PhotoImage(foto)

<<<<<<< HEAD
	fondo = tk.Label(ventana, image = img)
	fondo.pack()

	ventana.mainloop()
=======
	fondo = tk.Label(interfaz, image = img)
	fondo.pack()

	interfaz.mainloop()
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
