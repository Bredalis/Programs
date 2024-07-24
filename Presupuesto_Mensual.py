
# Librerias

import pandas as pd
import sqlite3 as sqlite
import matplotlib.pyplot as plt

# Conectar a BBDD

bbdd_presupuesto = sqlite.connect("Presupuesto.db")

# Obtener todas las columnas de las tablas

presupuesto = pd.read_sql("SELECT MONTH, SPENDING, INCOME FROM Monthly", bbdd_presupuesto)
print(f"Presupuesto: \n{presupuesto}")

# Mostrar gastos mensuales

def gastos():

	plt.bar(presupuesto.MONTH, presupuesto.SPENDING, color = "pink")
	plt.title("Gastos")
	plt.show()

# Mostrar presupuesto mensual

gastos()

plt.bar(presupuesto.MONTH, presupuesto.INCOME, color = "pink")
plt.title("Presupuesto Mensual (Ingresos)")
plt.show()