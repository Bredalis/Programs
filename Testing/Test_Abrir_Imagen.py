
from Ruta_Scripts import *

# Librerías
from unittest.mock import patch
import tkinter as tk
from Abrir_Imagen import CerrarVentana

# Prueba para verificar que se maneje correctamente una imagen
def test_agregar_imagen():
	ventana = tk.Tk()
	clase_ventana = CerrarVentana(ventana)

	# Simular la selección de una imagen
	with patch("tkinter.filedialog.askopenfilename", return_value = "path/to/image.png"):
		clase_ventana.agregar_imagen()  

	assert clase_ventana.x.winfo_exists()

# Prueba para la verificar que se maneje correctamente el cierre
def test_salir():
    ventana = tk.Tk()
    clase_ventana = CerrarVentana(ventana)
    clase_ventana.salir_ventana()

    # Verificar que la ventana principal y la secundaria han sido destruidas
    try:
        ventana.winfo_exists()
        ventana_destruida = False
    
    except tk.TclError:
        ventana_destruida = True

    assert ventana_destruida