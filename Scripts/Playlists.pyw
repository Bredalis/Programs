
# Librerías
import pygame
import tkinter as tk
from tkinter import filedialog

class ReproductorDeMusica:
	def __init__(self, ventana):
		self.ventana = ventana
		self.ventana.title("PlayList")
		self.ventana.geometry("210x100")
		self.ventana.resizable(0, 0)
		self.ventana.config(bg = "#edd269")
		self.ventana.iconbitmap("../IMG/Playlists.ico")
		self.playlist = [] 

		pygame.init()
		pygame.mixer.init()

		# Botones
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

	def pausar(self):
		pygame.mixer.music.pause()

	def reanudar(self):
		pygame.mixer.music.unpause()

if __name__ == "__main__":
	ventana = tk.Tk()
	app = ReproductorDeMusica(ventana)
	ventana.mainloop()