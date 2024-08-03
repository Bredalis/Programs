
# Programa que remueve
# simbolos innecesarios

class RemplazarSimbolos:
	def __init__(self, url_archivo):

		self.url = url_archivo

	def abrir_archivo(self):
		self.archivo = open(self.url).read()

	def remplazar_simbolos(self, simbolo, simbolo_nuevo):
		self.archivo_nuevo = self.archivo.replace(simbolo, simbolo_nuevo)

	def guardar_archivo(self):

		with open(self.url, "w") as archivo:
			archivo.write(self.archivo_nuevo)

	def mostrar_archivo(self):
		print(f"\nArchivo anterior:\n {self.archivo}")
		print(f"\nArchivo nuevo:\n {self.archivo_nuevo}")

# Modifica la url y los simbolos

# archivo = RemplazarSimbolos("C:/Users/Bradalis/Downloads/Borrar.txt")
# archivo.abrir_archivo()
# archivo.remplazar_simbolos("#", " ")
# archivo.guardar_archivo()
# archivo.mostrar_archivo()