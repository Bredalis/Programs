
# Librerías

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