
# Programa que reproduce 
# musica en mp3

class ReproductorDeMusica:

	def __init__(self, interfaz):

		# Propiedades de la interfaz
		
		self.interfaz = interfaz
		self.interfaz.title("PlayList")
		self.interfaz.geometry("210x100")
		self.interfaz.resizable(0,0)
		self.interfaz.config(bg = "#edd269")
		self.icono = "Playlists.ico"
		self.interfaz.iconbitmap(self.icono)

		self.playlist = [] # Lista de musica

		pygame.init()
		pygame.mixer.init()

		# Botones

		self.cargar = tk.Button(self.interfaz, text = "Cargar", 
			bg = "#aee239", command = self.cargar).pack()

		self.reproducir = tk.Button(self.interfaz, text = "Reproducir", 
			bg = "#aee239", command = self.reproducir).pack()

		self.pausar = tk.Button(self.interfaz, text = "Pausar", 
			bg = "#aee239", command = self.pausar).pack()

		self.reanudar = tk.Button(self.interfaz, text = "Reanudar", 
			bg = "#aee239", command = self.reanudar).pack()

	# Funcion que busca y guarda la musica

	def cargar(self):
		cancion = filedialog.askopenfilename(
			title = "Musica", initialdir = "C:", filetypes = (
				("Archivo de audio", "*.mp3"), ("todos los archivos", "*.*")))

		self.playlist.append(cancion) # Se guarda aqui

	# Funcion que reproduce la musica

	def reproducir(self):
		if len(self.playlist) == 0:
			return

		pygame.mixer.music.load(self.playlist[0])
		pygame.mixer.music.play()

	# Pausa la musica

	def pausar(self):
		pygame.mixer.music.pause()

	# Reanuda la musica

	def reanudar(self):
		pygame.mixer.music.unpause()

if __name__ == "__main__":

	# Librerias

	import pygame
	import tkinter as tk
	from tkinter import filedialog

	# Interfaz

	interfaz = tk.Tk()
	app = ReproductorDeMusica(interfaz)
	interfaz.mainloop()