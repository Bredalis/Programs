
from Ruta_Scripts import *

# Librería de testing
import unittest
import tkinter as tk
import Calculadora

# Clase de testing unitario
class TestCalculadora(unittest.TestCase):

	# Evaluar cada funcionalidad del programa
	def setUp(self):
		Calculadora.mi_entry = tk.Entry()
		Calculadora.mi_entry.grid(column = 0, row = 0)
		Calculadora.mi_entry.delete(0, tk.END)

	def test_reclick(self):
		Calculadora.reclick(5)
		self.assertEqual(Calculadora.mi_entry.get(), "5")

	def test_reclick_concatenacion(self):
		Calculadora.reclick(1)
		Calculadora.reclick(2)
		Calculadora.reclick(3)
		self.assertEqual(Calculadora.mi_entry.get(), "123")

	def test_limpiar(self):
		Calculadora.reclick(5)
		Calculadora.limpiar()
		self.assertEqual(Calculadora.mi_entry.get(), "")

	def test_operaciones_aritmeticas(self):
		Calculadora.reclick(10)
		Calculadora.operaciones_aritmeticas("+")
		self.assertEqual(Calculadora.numero_1, 10.0)
		self.assertEqual(Calculadora.operacion, "+")

	def test_resultado_suma(self):
		Calculadora.reclick(1)
		Calculadora.operaciones_aritmeticas("+")
		Calculadora.reclick(2)
		Calculadora.resultado()
		self.assertEqual(Calculadora.mi_entry.get(), "3.0")

	def test_resultado_resta(self):
		Calculadora.reclick(19)
		Calculadora.operaciones_aritmeticas("-")
		Calculadora.reclick(10)
		Calculadora.resultado()
		self.assertEqual(Calculadora.mi_entry.get(), "9.0")

	def test_resultado_multiplicacion(self):
		Calculadora.reclick(2)
		Calculadora.operaciones_aritmeticas("*")
		Calculadora.reclick(2)
		Calculadora.resultado()
		self.assertEqual(Calculadora.mi_entry.get(), "4.0")

	def test_resultado_division(self):
		Calculadora.reclick(1)
		Calculadora.operaciones_aritmeticas("/")
		Calculadora.reclick(1)
		Calculadora.resultado()
		self.assertEqual(Calculadora.mi_entry.get(), "1.0")

	def test_resultado_division_por_cero(self):
		Calculadora.reclick(10)
		Calculadora.operaciones_aritmeticas("/")
		Calculadora.reclick(0)
		Calculadora.resultado()
		self.assertEqual(Calculadora.mi_entry.get(), "Error")

	def test_resultado_binario_natural(self):
		Calculadora.reclick(10)
		Calculadora.operaciones_aritmeticas("B")
		Calculadora.resultado()
		self.assertEqual(Calculadora.mi_entry.get(), "1010")

	def test_resultado_binario_negativo(self):
		Calculadora.reclick(-3)
		Calculadora.operaciones_aritmeticas("B")
		Calculadora.resultado()
		self.assertEqual(Calculadora.mi_entry.get(), "-11")

if __name__ == "__main__":
	unittest.main()