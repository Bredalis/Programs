
import matplotlib.pyplot as plt

class Pastel:
	def __init__(self):
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