
import matplotlib.pyplot as plt

class Pastel:
	def __init__(self):

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