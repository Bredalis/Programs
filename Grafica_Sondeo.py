
# Grafica de un
# sondeo estudiantil

import pandas as pd
import matplotlib.pyplot as plt

class Grafica:

	def crear_df(self):
		self.df = pd.DataFrame({
			"Porcientos": [60, 25, 15],
			"Problematicas": ["Falta de equipos informáticos", 
			"Contaminación", "Falta de dispositivos"],
			"Colores": ["skyblue", "#58D68D", "#F9E79F"]
		})

	def crear_barras(self):
		plt.bar(self.df.Problematicas, self.df.Porcientos, 
			color = self.df.Colores)
		plt.show()

	def crear_pastel(self):
		plt.pie(self.df.Porcientos, labels = self.df.Problematicas,
			autopct = "%1.1f%%", startangle = 90)
		plt.show()

	def propiedades(self):
		plt.title("Problemáticas En Nuestra Comunidad Educativa")

barras = Grafica() 
barras.crear_df()
barras.propiedades()
barras.crear_barras()

pastel = Grafica()
pastel.crear_df()
pastel.propiedades()
pastel.crear_pastel()