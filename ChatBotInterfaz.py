
# Librerias

import openai
import shutil
import requests
import tkinter as tk
from tkinter import scrolledtext

ventana = tk.Tk()
ventana.title("ChatBot")
ventana.geometry("1075x490")
ventana.resizable(0, 0)
ventana.config(bg = "#566573")
ventana.iconbitmap("AI.ico")

# Variables

opcion = tk.IntVar()
url = ""

openai.api_key = "sk-proj-BFO5TeYjGjUrFcfMwVy9T3BlbkFJd61BI454CJuNNvmOiOFv"
modelo = "gpt-3.5-turbo"

# Funciones

def Modelo():

	contexto = input("Ingrese el contexto del modelo: ")
	pregunta = barra_preguntas.get("1.0", tk.END)

	mensajes = [
		{"role":"system", "content": contexto},
		{"role":"user", "content": pregunta}
	]

	respuesta = openai.chat.completions.create(
		model = modelo,
		messages = mensajes,
		temperature = 1,
		max_tokens = 1000
	)

	caja_de_chat.insert(tk.END, "\nModelo: " + respuesta.choices[0].message.content)

def Dalle():

	# Crear imagen

	prompt_imagen = barra_preguntas.get("1.0", tk.END)
	caja_de_chat.insert(tk.END, "\n\nTu: " + prompt_imagen)
	HistorialDePreguntas()
	barra_preguntas.delete("1.0", tk.END)

	imagen = openai.images.generate(
		prompt = prompt_imagen,
		n = 1,
		size = "1024x1024"
	)

	url_imagen = imagen.data[0].url
	foto = requests.get(url_imagen, stream = True)

	# Guardar

	nombre = input("Ingrese el nombre para la imagen: ")
	nombre = nombre + ".jpg"

	if foto.status_code == 200:
		with open(nombre, "wb") as f:
			shutil.copyfileobj(foto.raw, f)
			caja_de_chat.insert(tk.END, "\n\nModelo: " + "¡La descarga fue un exito!")
	else:
		caja_de_chat.insert(tk.END, "\n\nModelo: " +  "Error al acceder a la imagen")

def Whisper():
	
	# Transcripcion

	url = input("Introduce la url del audio: ")
	caja_de_chat.insert(tk.END, "\n\nTu: " + url)
	caja_de_preguntas.insert(tk.END, "\nPregunta: " + url)

	with open(url, "rb") as audio:
		transcripcion = openai.audio.transcriptions.create(
			model = "whisper-1", 
			file = audio
		)

	transcripcion = transcripcion.text
	caja_de_chat.insert(tk.END, "\n\nModelo: " + f"\nTranscripcion: \n{transcripcion}")

def NuevoChat():

	if opcion.get() == 1:
		[caja_de_chat.delete("1.0", tk.END), caja_de_preguntas.delete("1.0", tk.END), 
		barra_preguntas.delete("1.0", tk.END), opcion.set(0)]

def HistorialDePreguntas():
	caja_de_preguntas.insert(tk.END, "\nPregunta: " + barra_preguntas.get("1.0", tk.END))

def Enviar(event = None):
    caja_de_chat.insert(tk.END, "\n\nTu: " + barra_preguntas.get("1.0", tk.END))

    HistorialDePreguntas()
    barra_preguntas.delete("1.0", tk.END)
    Modelo()

# Marco de fondo

marco = tk.Frame(ventana, padx = 120, pady = 400, bg = "#2C3E50")
marco.place(x = 0, y = 0)

tk.Label(marco, bg = "#2C3E50", fg = "white").pack()

# Caja de preguntas

scrollbar_preguntas = tk.Scrollbar(ventana, orient = "vertical")
caja_de_preguntas = scrolledtext.ScrolledText(ventana, wrap = tk.WORD, yscrollcommand = scrollbar_preguntas.set, 
	bg = "#2C3E50", fg = "white", width = 27)

caja_de_preguntas.place(x = 10, y = 100)
scrollbar_preguntas.config(command = caja_de_preguntas.yview)

# Historial

tk.Label(ventana, text = "Historial", bg = "#2C3E50", fg = "white", font = ("Ariel", 16)).place(x = 70, y = 60)

tk.Checkbutton(ventana, text = "Nuevo Chat", bg = "#2C3E50", fg = "white", activebackground = "#2C3E50", 
	variable = opcion, onvalue = 1, offvalue = 0, command = NuevoChat).place(x = 1, y = 5)

tk.Checkbutton(ventana, text = "Dall-e", bg = "#2C3E50", fg = "white", activebackground = "#2C3E50", 
	variable = opcion, onvalue = 1, offvalue = 0, command = Dalle).place(x = 100, y = 5)

tk.Checkbutton(ventana, text = "Whisper", bg = "#2C3E50", fg = "white", activebackground = "#2C3E50", 
	variable = opcion, onvalue = 1, offvalue = 0, command = Whisper).place(x = 165, y = 5)

# Chat

tk.Label(ventana, text = "Chat", bg = "#566573", fg = "white", font = ("Ariel", 16)).place(x = 650, y = 10)

# Caja de texto

scrollbar = tk.Scrollbar(ventana, orient = "vertical")
caja_de_chat = scrolledtext.ScrolledText(ventana, wrap = tk.WORD, yscrollcommand = scrollbar.set, 
	bg = "#5D6D7E", fg = "white", width = 100, height = 20)

caja_de_chat.place(x = 248, y = 50)
scrollbar.config(command = caja_de_chat.yview)

# Barra de preguntas  

barra_preguntas = tk.Text(ventana, wrap = tk.WORD, bg = "#5D6D7E", fg = "white", width = 92, height = 3)
barra_preguntas.place(x = 248, y = 430)

barra_preguntas.bind("<Return>", Enviar)

tk.Button(ventana, text = "Enviar", bg = "#5D6D7E", fg = "white", 
	width = 10, height = 3, command = Enviar).place(x = 990, y = 430)

ventana.mainloop()