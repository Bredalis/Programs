
# Reproductor de musica en mp3

# Librerías

import pygame
import tkinter as tk
from tkinter import filedialog

class ReproductorDeMusica:
	def __init__(self, interfaz):

		# Propiedades de la interfaz
		
		self.interfaz = interfaz
		self.interfaz.title("PlayList")
		self.interfaz.geometry("210x100")
		self.interfaz.resizable(0,0)
		self.interfaz.config(bg = "#edd269")
		self.interfaz.iconbitmap("../IMG/Playlists.ico")

		self.playlist = [] 

		pygame.init()
		pygame.mixer.init()

		# Botones

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

	def pausar(self):
		pygame.mixer.music.pause()

	def reanudar(self):
		pygame.mixer.music.unpause()

if __name__ == "__main__":

	interfaz = tk.Tk()
	app = ReproductorDeMusica(interfaz)
	interfaz.mainloop()