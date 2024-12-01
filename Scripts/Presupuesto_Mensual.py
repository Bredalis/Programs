
# Librerías
<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt

# Obtener el dataset
presupuesto_mensual = pd.read_csv("../BBDD/Presupuesto_Mensual.csv")
print(presupuesto_mensual)

# Mostrar las distintas gráficas
def graficar_datos(y):
	plt.bar(presupuesto_mensual.MES, presupuesto_mensual[y], color = "pink")
	plt.title("Presupuesto Mensual - " + y)
	plt.ylabel(y)
	plt.xticks(rotation = 45)
	plt.show()

# Mostrar las gráficas
graficar_datos("INGRESOS")
graficar_datos("GASTOS")
graficar_datos("PRESTAMOS")
graficar_datos("TOTAL INGRESOS")
=======

import pandas as pd
import matplotlib.pyplot as plt

# Conectar con el dataset

presupuesto_mensual = pd.read_csv("../BBDD/Presupuesto_Mensual.csv")
print(presupuesto_mensual)

# Función para mostrar las distintas gráficas

def graficar_datos(y, titulo):

	plt.bar(presupuesto_mensual.MES, presupuesto_mensual[y], color = "pink")
	plt.title(titulo + y)
	plt.show()

# Mostrar las gráficas

graficar_datos("INGRESOS", "Presupuesto Mensual - ")
graficar_datos("GASTOS", "Presupuesto Mensual - ")
graficar_datos("TOTAL INGRESOS", "Presupuesto Mensual - ")
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
