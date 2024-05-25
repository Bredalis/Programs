
# Rendimiento de los alumnos
# Evaluacion de las calificaciones
# con respecto a las horas de estudio

# Librerias

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from Metodos_Modelo import *

# Metodos

metodos = metodosParaModelos()

# Lectura de datos

df = pd.read_csv("Rendimiento_Escolar.csv")

print(df)
print(df.shape)

# Division de datos

# Entrenamiento

X_train = df.loc[:99, ["calificaciones"]]
y_train = df.loc[:99, ["horas_de_estudios"]]

print(len(X_train))
print(len(y_train))

print(X_train)
print(y_train)

# Pruebas

X_test = df.loc[100:, ["calificaciones"]]
y_test = df.loc[100:, ["horas_de_estudios"]]

print(len(X_test))
print(len(y_test))

print(X_test)
print(y_test)

# Modelo

modelo = LinearRegression(fit_intercept = True)

metodos.entrenamiento(modelo, X_train, y_train)

y_hat = modelo.predict(X_test)

# Metricas de evaluacion

metodos.metricas_regresion(y_test, y_hat)

# Grafica sin prediccion

plt.rcParams["figure.figsize"] = (10, 5)

df.plot.scatter(x = "calificaciones", y = "horas_de_estudios")
plt.show()

# Grafica con prediccion

plt.scatter(X_test, y_test, label = "Datos")
plt.plot(X_test, y_hat, c = "red", label = "Predicciones")

plt.title("Calificaciones y horas de estudios")
plt.legend()
plt.show()