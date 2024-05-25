
import tkinter as tk
from tkinter import ttk

def agregar_prioridades():
	lista_prioridades.insert("", tk.END, values = (entry_articulos.get()))

def agregar_costo():
	lista_costo.insert("", tk.END, values = (entry_articulos.get()))

ventana = tk.Tk()
ventana.title("Lista De Compras")
ventana.geometry("500x430")
ventana.resizable(0, 0)
ventana.iconbitmap("Compras.ico")

ttk.Label(ventana, text = "Lista De Compras", font = ("Verdana", 15)).pack(pady = 30)

# Entry para ingresar los articulos
entry_articulos = ttk.Entry(ventana)
entry_articulos.pack()

ttk.Button(ventana, text = "Prioridades", cursor = "hand2", 
	command = agregar_prioridades).place(x = 160, y = 120)
ttk.Button(ventana, text = "Costo", cursor = "hand2", 
	command = agregar_costo).place(x = 260, y = 120)

# Creacion de las listas
lista_prioridades = ttk.Treeview(ventana, columns = ("Prioridades"), 
	show = "headings")

lista_prioridades.heading("Prioridades", text = "Prioridades")

# Configurar ancho de las columnas
lista_prioridades.column("Prioridades", width = 200)
lista_prioridades.place(x = 55, y = 160)

lista_costo = ttk.Treeview(ventana, columns = ("Costo"), 
	show = "headings")

lista_costo.heading("Costo", text = "Costo")

# Configurar ancho de las columnas
lista_costo.column("Costo", width = 200)
lista_costo.place(x = 255, y = 160)

ventana.mainloop()