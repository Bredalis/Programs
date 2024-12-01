
# Librerías

import tkinter as tk
import sqlite3 as sqlite

ventana = tk.Tk()
ventana.title("Formulario")
ventana.resizable(0, 0)
ventana.config(bg = "pink")
ventana.geometry("340x310")

ventana.iconbitmap("../IMG/Registro_2.ico")

# Guardar datos en la bbdd

def manipular_boton(contenedores):

	for i in contenedores:
		if i.get() == "":
			boton.config(text = "Guardado")

def limpiar_datos(contenedores):
	for i in contenedores:
		i.set("")

def guardar_datos(contenedores):

	bbdd = sqlite.connect("../BBDD/Formulario.db")
	cursor = bbdd.cursor()
	instruccion = f"INSERT INTO Formulario(Nombre, Edad, Hobby) VALUES('{nombre.get()}', {edad.get()}, '{hobby.get()}')"
	cursor.execute(instruccion)

	limpiar_datos(contenedores)
	manipular_boton(contenedores)

	bbdd.commit()
	bbdd.close()

tk.Label(ventana, text = "Formulario", bg = "pink", 
	pady = 30, font = (25)).pack()

# Contenedores de informacion

nombre = tk.StringVar()
edad = tk.StringVar()
hobby = tk.StringVar()
contenedores = [nombre, edad, hobby]

# Etiquetas y campos a llenar

def etiquetas(texto, variable):
	tk.Label(ventana, text = texto, bg = "pink").pack()
	barra_nombre = tk.Entry(ventana, textvariable = variable)
	barra_nombre.pack(pady = 10)

etiquetas("Nombre:", nombre)
etiquetas("Edad:", edad)
etiquetas("Hobby:", hobby)

# Boton para guardar

boton = tk.Button(ventana, text = "Guardar", 
	command = lambda: guardar_datos(contenedores))
boton.place(x = 200, y = 272)

ventana.mainloop()