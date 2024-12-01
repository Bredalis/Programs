
import matplotlib.pyplot as plt

class Pastel:
	def __init__(self):
<<<<<<< HEAD
		self.nombres = []
		self.cantidades = []
		self.pregunta = ""

	def ejecucion(self):
		print("\nGráfica de pastel con los datos ingresados")

		while self.pregunta.lower() != "no":
			try:
				self.nombre = input("Ingrese el nombre: ")	
				self.porcentaje = int(input("Ingrese el porcentaje: "))
				
				self.nombres.append(self.nombre)
				self.cantidades.append(self.porcentaje)
			except Exception as e:
				print(f"Error inesperado: {e}")

			finally:
				self.pregunta = input("\n¿Quieres seguir ingresando datos? (si/no): ")

	def grafica(self):
		plt.pie(self.cantidades, labels = self.nombres)
		plt.title("Gráfica de Pastel")
		plt.show()

if __name__ == "__main__":
	grafica_pastel = Pastel()
	grafica_pastel.ejecucion()
	grafica_pastel.grafica()
=======

		self.lista_nombres = []
		self.lista_cantidades = []
		self.pregunta = ""

	def ejecucion(self):

		while self.pregunta.lower() != "no":

			try:
				self.nombres = input("Nombre: ")	
				self.cantidades = int(input("Porcentaje: "))
				
				self.lista_nombres.append(self.nombres)
				self.lista_cantidades.append(self.cantidades)

			except Exception as e:
				print(f"Error: {e}")

			finally:
				self.pregunta = input("¿Quieres seguir ingresando integrantes?: ")

	def grafica(self):

		plt.pie(self.lista_cantidades, labels = self.lista_nombres)

		plt.title("Grafica de Pastel")
		plt.show()

if __name__ == "__main__":

	pastel = Pastel()
	pastel.ejecucion()
	pastel.grafica()
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
