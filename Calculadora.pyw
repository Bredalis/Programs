
import tkinter as tk
import math

ventana = tk.Tk()
ventana.geometry("245x245") 
ventana.title("CALCULATOR")
ventana.resizable(0, 0)
ventana.config(bg = "white")

ventana.iconbitmap("Calculadora.ico")

contenido = open("Manual.txt").read()
exec(contenido)

def clean():
	mi_entry.delete(0, tk.END)

def reclick(valor):
	
	Anterior = mi_entry.get()

	mi_entry.delete(0, tk.END)
	mi_entry.insert(0, str(Anterior + str(valor)))

def binario():

	global numero_1
	global operacion

	numero_1 = mi_entry.get()
	numero_1 = int(numero_1)

	operacion = "B"

def suma():

    global numero_1
    global operacion

    numero_1 = mi_entry.get()
    numero_1 = float(numero_1)

    mi_entry.delete(0, tk.END)

    operacion = "+"

def resta():

	global numero_1 
	global operacion

	numero_1 = mi_entry.get()
	numero_1 = float(numero_1)

	mi_entry.delete(0, tk.END)

	operacion = "-"

def multiplicacion():

	global numero_1
	global operacion

	numero_1 = mi_entry.get()
	numero_1 = float(numero_1)

	mi_entry.delete(0, tk.END)

	operacion = "*"

def division():

	global numero_1
	global operacion

	numero_1 = mi_entry.get()
	numero_1 = float(numero_1)

	mi_entry.delete(0, tk.END)

	operacion = "/"

def potencia():

	global numero_1
	global operacion

	numero_1 = mi_entry.get()
	numero_1 = float(numero_1)

	mi_entry.delete(0, tk.END)

	operacion = "^"

def radicacion():

	global numero_1
	global operacion

	numero_1 = mi_entry.get()
	numero_1 = int(numero_1)

	operacion = "√"
	
def resultado():

	global numero_2
	
	numero_2 = mi_entry.get()
	numero_2 = float(numero_2)

	mi_entry.delete(0, tk.END)

	if operacion == "+" :

		mi_entry.insert(0, numero_1 + numero_2)

	if operacion == "-" :

		mi_entry.insert(0, numero_1 - numero_2)

	if operacion == "*" :

		mi_entry.insert(0, numero_1 * numero_2)

	if operacion == "^" :
		
		mi_entry.insert(0, numero_1 ** numero_2)

	if operacion == "B":

		mi_entry.insert(0, bin(numero_1)[2:])

	if operacion == "/":

		try:

			mi_entry.insert(0, numero_1 / numero_2)

		except ZeroDivisionError:

			mi_entry.insert(0, "Error")

	if operacion == "√":

		mi_entry.insert(0, math.sqrt(numero_1))

condicion = True
texto = tk.IntVar().set("")
numero_1 = ""
numero_2 = ""
operacion = ""

mi_entry = tk.Entry(ventana, textvariable = texto, width = 40, justify = "right", bg = "white")
mi_entry.grid(column = 0, row = 0, columnspan = 5)

tk.Button(ventana, text = "1", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = lambda: reclick(1)).grid(column = 1, row = 1, pady = 10)
tk.Button(ventana, text = "2", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = lambda: reclick(2)).grid(column = 2, row = 1, pady = 10)
tk.Button(ventana, text = "3", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = lambda: reclick(3)).grid(column = 3, row = 1, pady = 10)

tk.Button(ventana, text = "4", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = lambda: reclick(4)).grid(column = 1, row = 2, pady = 10)
tk.Button(ventana, text = "5", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = lambda: reclick(5)).grid(column = 2, row = 2, pady = 10)
tk.Button(ventana, text = "6", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = lambda: reclick(6)).grid(column = 3, row = 2, pady = 10)

tk.Button(ventana, text = "7", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = lambda: reclick(7)).grid(column = 1, row = 3, pady = 10)
tk.Button(ventana, text = "8", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = lambda: reclick(8)).grid(column = 2, row = 3, pady = 10)
tk.Button(ventana, text = "9", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = lambda: reclick(9)).grid(column = 3, row = 3, pady = 10)

tk.Button(ventana, text = "0", bg = "#A569BD", cursor  = "hand2", width = 5, activebackground = "pink", command = lambda: reclick(0)).grid (column = 1, row = 4, pady = 10)
tk.Button(ventana, text = "+", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = suma).grid(column = 4, row = 1, pady = 10)
tk.Button(ventana, text = "x", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink",command = multiplicacion).grid(column = 4, row = 2, pady = 10)

tk.Button(ventana, text = "÷", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = division).grid(column = 3, row = 4, pady = 10)
tk.Button(ventana, text = "-", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = resta).grid(column = 4, row = 3, pady = 10)
tk.Button(ventana, text = "π", bg = "#A569BD", cursor  = "hand2", width = 5, activebackground = "pink", command = lambda: reclick(math.pi)).grid(column = 2, row = 4, pady = 10)
tk.Button(ventana, text = "=", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = resultado).grid(column = 4, row = 4, pady = 10)

tk.Button(ventana, text = "B", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = binario).grid(column = 1, row = 5, pady = 10)
tk.Button(ventana, text = "√", bg = "#A569BD", cursor  = "hand2", width = 5, activebackground = "pink", command = radicacion).grid(column = 2, row = 5, pady = 10)
tk.Button(ventana, text = "⌦", bg = "#A569BD", cursor  = "hand2", width = 5, activebackground = "pink", command = clean).grid(column = 3, row = 5, pady = 10)
tk.Button(ventana, text = "^", bg = "#A569BD", cursor = "hand2", width = 5, activebackground = "pink", command = potencia).grid(column = 4, row = 5, pady = 10)

class Cerrar():

    def __init__(self, herencia):

        self.x = tk.Toplevel(herencia)
        self.x.title("Salir")

        self.herencia = herencia
        
        tk.Label(self.x, text = "¿Quieres cambiar de color?").grid(row = 0, column = 0, columnspan = 2)

        self.si = tk.Button(self.x, text = "Si", activebackground = "pink", command = self.color)
        self.si.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.no = tk.Button(self.x, text = "No", activebackground = "pink", command = self.salir)        
        self.no.grid(row = 1, column = 1, padx = 5, pady = 5)

    def color(self):
        

    	global condicion

    	if condicion:

    		ventana.config(bg = "black")

    		mi_entry.config(bg = "black")
    		mi_entry.config(fg = "white")

    		condicion = False

    	else:

    		ventana.config(bg = "white")
    		mi_entry.config(bg = "white")
    		mi_entry.config(fg = "black")

    		condicion = True    	

    def salir(self):

        self.x.destroy()
        self.herencia.destroy()

class Calculadora():

    def __init__(self, herencia):

        self.herencia = herencia
        self.herencia.protocol("WM_DELETE_WINDOW", self.Al_Cerrar)

    def Al_Cerrar(self):

        clase = Cerrar(ventana)

        self.herencia.wait_window(clase.x)

if __name__ == "__main__":

    clase = Calculadora(ventana)

manual("Manual_Calculadora.txt")

ventana.mainloop()