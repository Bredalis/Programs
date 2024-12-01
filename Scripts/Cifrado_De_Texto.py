
import tkinter as tk

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