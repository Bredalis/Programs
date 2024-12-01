
import tkinter as tk
import math

ventana = tk.Tk()
ventana.geometry("245x245") 
ventana.title("CALCULATOR")
ventana.resizable(0, 0)
ventana.config(bg = "white")
ventana.iconbitmap("../IMG/Calculadora.ico")

contenido = open("../TXT/Manual.txt").read()
exec(contenido)

# Cerrar la ventana 
<<<<<<< HEAD
class Cerrar:
    def __init__(self, herencia):
=======

class Cerrar:
    def __init__(self, herencia):

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
        self.x = tk.Toplevel(herencia)
        self.x.title("Salir")
        self.x.geometry("200x100")
        self.x.resizable(0, 0)

        self.herencia = herencia
        
<<<<<<< HEAD
        tk.Label(self.x, text = "¿Quieres cambiar de\ncolor?").pack(pady = 5)
=======
        tk.Label(self.x, text = "¿Quieres cambiar de \ncolor?").pack(pady = 5)

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
        tk.Button(self.x, text = "Si", 
            activebackground = "skyblue", command = self.color).place(x = 60, y = 50)

        tk.Button(self.x, text = "No", 
            activebackground = "skyblue", command = self.salir).place(x = 100, y = 50)

    def color(self):
<<<<<<< HEAD
    	global condicion

    	if condicion:
=======
        
    	global condicion

    	if condicion:

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
    		ventana.config(bg = "black")
    		mi_entry.config(bg = "black")
    		mi_entry.config(fg = "white")

    		condicion = False

    	else:
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
    		ventana.config(bg = "white")
    		mi_entry.config(bg = "white")
    		mi_entry.config(fg = "black")

    		condicion = True    	
 
    def salir(self):
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
        self.x.destroy()
        self.herencia.destroy()

class Calculadora():
    def __init__(self, herencia):
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
        self.herencia = herencia
        self.herencia.protocol("WM_DELETE_WINDOW", self.al_cerrar)

    def al_cerrar(self):
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
        clase = Cerrar(ventana)
        self.herencia.wait_window(clase.x)

def limpiar():
	mi_entry.delete(0, tk.END)

def reclick(valor):
<<<<<<< HEAD
=======
	
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
	anterior = mi_entry.get()

	mi_entry.delete(0, tk.END)
	mi_entry.insert(0, str(anterior + str(valor)))

def binario():
<<<<<<< HEAD
	global numero_1
	global operacion

	numero_1 = int(mi_entry.get())
	operacion = "B"

def operaciones_aritmeticas(signo_operacion):
=======

	global numero_1
	global operacion

	numero_1 = mi_entry.get()
	numero_1 = int(numero_1)

	operacion = "B"

def operaciones_aritmeticas(signo_operacion):

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
	global numero_1
	global operacion

	numero_1 = mi_entry.get()
	numero_1 = float(numero_1)

	mi_entry.delete(0, tk.END)
	operacion = signo_operacion
	
def resultado():
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
	global numero_2
	numero_2 = mi_entry.get()

	if operacion == "B":  # Operación binaria
		try:
<<<<<<< HEAD

			if numero_1 < 0:
				# Convertir a binario negativo
				numero_binario = f"-{bin(int(numero_1))[3:]}"
			else:
				numero_binario = bin(int(numero_1))[2:]
			
=======
			numero_binario = bin(int(numero_1))[2:]  # Convertir a binario
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
			mi_entry.delete(0, tk.END)
			mi_entry.insert(0, numero_binario)
        
		except ValueError:
		    mi_entry.delete(0, tk.END)
		    mi_entry.insert(0, "Error")
<<<<<<< HEAD

=======
	
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
	else:
		try:
		    numero_2 = float(numero_2)
		    if operacion == "+":
		        resultado = numero_1 + numero_2
		    
		    elif operacion == "-":
		        resultado = numero_1 - numero_2
		    
		    elif operacion == "*":
		        resultado = numero_1 * numero_2
		    
		    elif operacion == "/":
		        if numero_2 == 0:
		            resultado = "Error"
		        else:
		            resultado = numero_1 / numero_2

		    mi_entry.delete(0, tk.END)
		    mi_entry.insert(0, str(resultado))
        
		except ValueError:
			mi_entry.delete(0, tk.END)
			mi_entry.insert(0, "Error")

condicion = True
texto = tk.IntVar().set("")
numero_1 = ""
numero_2 = ""
operacion = ""

mi_entry = tk.Entry(ventana, textvariable = texto, width = 40, justify = "right", bg = "white")
mi_entry.grid(column = 0, row = 0, columnspan = 5)

def crear_boton(texto, funcion, colum, fila):
<<<<<<< HEAD
=======

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
	tk.Button(ventana, text = texto, bg = "#A569BD", cursor = "hand2", width = 5, 
		activebackground = "pink", 
		command = funcion).grid(column = colum, row = fila, pady = 10)

<<<<<<< HEAD
# Botones numéricos
=======
# Botones numericos

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
crear_boton("1", lambda: reclick(1), 1, 1)
crear_boton("2", lambda: reclick(2), 2, 1)
crear_boton("3", lambda: reclick(3), 3, 1)
crear_boton("4", lambda: reclick(4), 1, 2)
crear_boton("5", lambda: reclick(5), 2, 2)
crear_boton("6", lambda: reclick(6), 3, 2)
crear_boton("7", lambda: reclick(7), 1, 3)
crear_boton("8", lambda: reclick(8), 2, 3)
crear_boton("9", lambda: reclick(9), 3, 3)
crear_boton("0", lambda: reclick(0), 1, 4)

<<<<<<< HEAD
# Botones de símbolos
=======
# Botones de simbolos

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
crear_boton("+", lambda: operaciones_aritmeticas("+"), 4, 1)
crear_boton("X", lambda: operaciones_aritmeticas("*"), 4, 2)
crear_boton("÷", lambda: operaciones_aritmeticas("/"), 3, 4)
crear_boton("-", lambda: operaciones_aritmeticas("-"), 4, 3)
crear_boton("π", lambda: reclick(math.pi), 2, 4)
crear_boton("=", resultado, 4, 4)
crear_boton("B", binario, 1, 5)
crear_boton("√", lambda: operaciones_aritmeticas("√"), 2, 5)
crear_boton("⌦", limpiar, 3, 5)
crear_boton("^", lambda: operaciones_aritmeticas("^"), 4, 5)

clase = Calculadora(ventana)
manual("../TXT/Manual_Calculadora.txt")
ventana.mainloop()