
import tkinter as tk

<<<<<<< HEAD
class CifradoDeTexto:
    def __init__(self, ventana):
        self.ventana = ventana
        self.booleano = True
        self.lista_contenidos = []

        self.ventana.title("Cifrado de Texto")
        self.ventana.geometry("400x180")
        self.ventana.resizable(0, 0)
        self.ventana.iconbitmap("../IMG/Python.ico")

        tk.Label(self.ventana, text = "Ingrese su texto:",
                 font = ("Times", 16, "italic"), pady = 12).pack()

        self.caja_texto = tk.StringVar()
        self.entry_texto = tk.Entry(self.ventana, font = ("Arial", 12), width = 25,
                                    textvariable = self.caja_texto)
        self.entry_texto.pack(pady = 25)

        self.boton = tk.Button(self.ventana, text = "Cifrar", font = ("Times", 12, "italic"),
                               cursor = "hand2", width = 10, command = self.cifrar_decifrar)
        self.boton.place(x = 225, y = 100)

    def cifrar_decifrar(self):
        if self.booleano:
            cifrado = len(self.caja_texto.get()) * "*"
            if "*" not in self.caja_texto.get():
                self.lista_contenidos.append(self.caja_texto.get())
            self.entry_texto.delete(0, tk.END)
            self.entry_texto.insert(0, cifrado)
            self.boton.config(text="Decifrar")
        else:
            self.entry_texto.delete(0, tk.END)
            self.entry_texto.insert(0, self.lista_contenidos[-1])
            self.boton.config(text="Cifrar")
        self.booleano = not self.booleano

if __name__ == "__main__":
    ventana = tk.Tk()
    app = CifradoDeTexto(ventana)
    ventana.mainloop()
=======
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
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
