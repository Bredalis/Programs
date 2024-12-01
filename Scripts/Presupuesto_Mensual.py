
# Librerías
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