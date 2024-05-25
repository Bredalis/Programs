
import tkinter as tk
import sqlite3 as sqlite
from math import floor

url = "Salud_Fisica.ico"

contenido = open("Manual.txt").read()
exec(contenido)

manual("Manual_IMC.txt", url)

ventana = tk.Tk()
ventana.title("IMC")
ventana.geometry("300x490")
ventana.resizable(0, 0)
ventana.config(bg = "#D6EAF8")
ventana.iconbitmap(url)

def conectar_bbdd():
	bbdd = sqlite.connect("Salud_Fisica.db")
	cursor = bbdd.cursor()

	instruccion = f"INSERT INTO IMC(Nombre, Peso, Altura, Salud_Fisica) VALUES('{nombre.get()}', '{peso.get()}', '{altura.get()}', '{etiqueta_resultado.cget("text")}');"
	cursor.execute(instruccion)

	bbdd.commit()
	bbdd.close()

booleano = True

def imc():

	global booleano

	resultado = floor(peso.get() / (altura.get() * altura.get()))

	if resultado < 18.5:
		etiqueta_resultado.config(text = f"IMC: {resultado}, Peso Bajo")

	elif resultado >= 18.5 and resultado <= 24.9:
		etiqueta_resultado.config(text = f"IMC: {resultado}, Peso Normal")

	elif resultado >= 25 and resultado <= 29.9:
		etiqueta_resultado.config(text = f"IMC: {resultado}, Sobrepeso")

	elif resultado >= 30:
		etiqueta_resultado.config(text = f"IMC: {resultado}, Obesidad")

	conectar_bbdd()

	if(booleano):
		boton.config(text = "Actualizado")
		booleano = False

	else:
		boton.config(text = "Actualizar")
		etiqueta_resultado.config(text = "")		
		booleano = True

# Elementos de la interfaz

nombre = tk.StringVar()
peso = tk.IntVar()
altura = tk.IntVar()

tk.Label(ventana, text = "Datos Para Determinar \n Su Salud Física", bg = "#D6EAF8", font = ("Comic Sans MS", 16)).pack(pady = 50)

tk.Label(ventana, text = "Nombre:", bg = "#D6EAF8", font = ("Comic Sans MS", 16)).pack()
entry_nombre = tk.Entry(ventana, textvariable = nombre)
entry_nombre.pack(ipady = 2)

tk.Label(ventana, text = "Peso:", bg = "#D6EAF8", font = ("Comic Sans MS", 16)).pack()
entry_peso = tk.Entry(ventana, textvariable = peso)
entry_peso.pack(ipady = 2)

tk.Label(ventana, text = "Altura:", bg = "#D6EAF8", font = ("Comic Sans MS", 16)).pack()
entry_altura = tk.Entry(ventana, textvariable = altura)
entry_altura.pack(ipady = 2)

boton = tk.Button(ventana, text = "Analizar", bg = "#D6EAF8", font = ("Comic Sans MS", 10), 
	bd = 2, cursor = "hand2", command = imc)
boton.pack()

etiqueta_resultado = tk.Label(ventana, bg = "#D6EAF8", font = ("Comic Sans MS", 12))
etiqueta_resultado.pack(pady = 15)

ventana.mainloop()