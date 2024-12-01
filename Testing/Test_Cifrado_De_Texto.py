
from Ruta_Scripts import *

import unittest
from Cifrado_De_Texto import CifradoDeTexto
import tkinter as tk

class TestCifradoDeTexto(unittest.TestCase):
    def setUp(self):
        self.ventana = tk.Tk()
        self.app = CifradoDeTexto(self.ventana)

    def tearDown(self):
        self.ventana.destroy()

    def test_cifrar(self):
        # Simular el valor del atributo "booleano"
        self.app.booleano = True  
        # Configurar texto de prueba
        self.app.caja_texto.set("Hola, Mundo")
        self.app.cifrar_decifrar()
        self.assertEqual(self.app.entry_texto.get(), "***********")

    def test_descifrar(self):
        # Simular el valor del atributo "booleano"
        self.app.booleano = False
        # Configurar texto de prueba
        self.app.lista_contenidos.append("Hola, Mundo")
        self.app.caja_texto.set("***********")
        self.app.cifrar_decifrar()
        self.assertEqual(self.app.entry_texto.get(), "Hola, Mundo")

if __name__ == "__main__":
    unittest.main()