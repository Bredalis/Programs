
# Libreria para ir a la ruta 
# donde estan los archivos

import sys
import os

# Insertar el directorio principal del archivo actual
sys.path.insert(0, os.path.abspath(os.path.join(
	os.path.dirname(__file__), "../Scripts")))