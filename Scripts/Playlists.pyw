
<<<<<<< HEAD
# Librerías
=======
# Reproductor de musica en mp3

# Librerías

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
import pygame
import tkinter as tk
from tkinter import filedialog

class ReproductorDeMusica:
<<<<<<< HEAD
	def __init__(self, ventana):
		self.ventana = ventana
		self.ventana.title("PlayList")
		self.ventana.geometry("210x100")
		self.ventana.resizable(0, 0)
		self.ventana.config(bg = "#edd269")
		self.ventana.iconbitmap("../IMG/Playlists.ico")
=======
	def __init__(self, interfaz):

		# Propiedades de la interfaz
		
		self.interfaz = interfaz
		self.interfaz.title("PlayList")
		self.interfaz.geometry("210x100")
		self.interfaz.resizable(0,0)
		self.interfaz.config(bg = "#edd269")
		self.interfaz.iconbitmap("../IMG/Playlists.ico")

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
		self.playlist = [] 

		pygame.init()
		pygame.mixer.init()

		# Botones
<<<<<<< HEAD
		tk.Button(self.ventana, text = "Cargar", bg = "#aee239", 
			command = self.cargar).pack()

		tk.Button(self.ventana, text = "Reproducir", bg = "#aee239", 
			command = self.reproducir).pack()

		tk.Button(self.ventana, text = "Pausar", bg = "#aee239", 
			command = self.pausar).pack()

		tk.Button(self.ventana, text = "Reanudar", bg = "#aee239", 
			command = self.reanudar).pack()

	def cargar(self):
		try:
			cancion = filedialog.askopenfilename(title = "Música", 
			initialdir = "C:", filetypes = (("Archivo de audio", "*.mp3"), 
				("todos los archivos", "*.*")))

			self.playlist.append(cancion) # Se guarda aquí
		except Exception as e:
			print(f"Error inesperado: {e}")
	
	def reproducir(self):
		try:
			if len(self.playlist) == 0:
				return

			pygame.mixer.music.load(self.playlist[0])
			pygame.mixer.music.play()
		except Exception as e:
			print(f"Error inesperado: {e}")
=======

		tk.Button(self.interfaz, text = "Cargar", bg = "#aee239", 
			command = self.cargar).pack()

		tk.Button(self.interfaz, text = "Reproducir", bg = "#aee239", 
			command = self.reproducir).pack()

		tk.Button(self.interfaz, text = "Pausar", bg = "#aee239", 
			command = self.pausar).pack()

		tk.Button(self.interfaz, text = "Reanudar", bg = "#aee239", 
			command = self.reanudar).pack()

	# Funcion que busca y guarda la musica

	def cargar(self):
		cancion = filedialog.askopenfilename(title = "Musica", 
			initialdir = "C:", filetypes = (("Archivo de audio", "*.mp3"), 
				("todos los archivos", "*.*")))

		self.playlist.append(cancion) # Se guarda aqui

	def reproducir(self):
		if len(self.playlist) == 0:
			return

		pygame.mixer.music.load(self.playlist[0])
		pygame.mixer.music.play()
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da

	def pausar(self):
		pygame.mixer.music.pause()

	def reanudar(self):
		pygame.mixer.music.unpause()

if __name__ == "__main__":
<<<<<<< HEAD
	ventana = tk.Tk()
	app = ReproductorDeMusica(ventana)
	ventana.mainloop()
=======

	interfaz = tk.Tk()
	app = ReproductorDeMusica(interfaz)
	interfaz.mainloop()
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
