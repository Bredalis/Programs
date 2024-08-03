
import tkinter as tk

ventana = tk.Tk()
ventana.title("Cifrado de Texto")
ventana.geometry("400x180")
ventana.resizable(0, 0)
ventana.iconbitmap("../IMG/Python.ico")

# Cifrar y decifrar

booleano = True
lista_contenidos = []

def cifrar():

	global booleano

	cifrado = len(caja_texto.get()) * "*"

	if "*" not in caja_texto.get():
		lista_contenidos.append(caja_texto.get())

	# Cifrar

	if booleano:

		entry_texto.delete(0, tk.END)
		entry_texto.insert(0, cifrado)

		boton.config(text = "Decifrar")
		booleano = False

	else:

		# Decifrar

		entry_texto.delete(0, tk.END)
		entry_texto.insert(0, lista_contenidos[-1])

		boton.config(text = "Cifrar")
		booleano = True

tk.Label(ventana, text = "Ingrese su texto:", font = ("Times", 16, "italic"), pady = 12).pack()

caja_texto = tk.StringVar()
entry_texto = tk.Entry(ventana, font = ("Arial", 12), width = 25, textvariable = caja_texto)
entry_texto.pack(pady = 25)

boton = tk.Button(ventana, text = "Cifrar", font = ("Times", 12, "italic"), cursor = "hand2", width = 10, command = cifrar)
boton.place(x = 225, y = 100)

ventana.mainloop()