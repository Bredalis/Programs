
ruta_scripts = open("Ruta_Scripts.py").read()
exec(ruta_scripts)

# Libreria para testing

import pytest
from unittest.mock import patch
import tkinter as tk
from Abrir_Imagen import Cerrar

# Prueba para verificar que se maneje correctamente una imagen

def test_agregar_imagen():
	ventana = tk.Tk()
	clase = Cerrar(ventana)

	# Simular la selección de una imagen
	with patch("tkinter.filedialog.askopenfilename", return_value = "path/to/image.png"):
		clase.agregar_imagen()  

	assert clase.x.winfo_exists() # La ventana secundaria debe existir

# Prueba para la verificar que se maneje correctamente el cierre

def test_salir():
    ventana = tk.Tk()
    clase = Cerrar(ventana)

    # Simular el cierre de la ventana
    clase.salir()

    # Verificar que la ventana principal y la secundaria han sido destruidas
   
    try:
        # Intentar verificar si la ventana principal aún existe
        ventana.winfo_exists()
        ventana_destruida = False
    
    except tk.TclError:
        ventana_destruida = True

    assert ventana_destruida  # La ventana principal debe haber sido destruida