
# Programa que predice el precio
# de las computadoras personales

# Librerias

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from Metodos_Modelo import *

# Metodo

metodo = metodosParaModelos()

# Lectura de datos

url = "Laptop_price.csv"
df = pd.read_csv(url)

print(df.head())

# Limpieza de datos
# Categoricos a binarios

df_numericos = df.drop(["Brand"], axis = 1)
print(df_numericos)

df_categorico = df.filter(["Brand"])
print(df_categorico)

df_categorico_numerico = pd.get_dummies(df_categorico, drop_first = True)
print(df_categorico_numerico)

df_nuevo = pd.concat([df_numericos, df_categorico_numerico], axis = 1)
print(df_nuevo)

# Division de datos

X = df_nuevo[["Processor_Speed", "RAM_Size", "Storage_Capacity", "Screen_Size", "Weight",
              "Brand_Asus", "Brand_Dell", "Brand_HP", "Brand_Lenovo"]]
y = df_nuevo["Price"]

print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

print(X_train)
print(X_test)
print(y_train)
print(y_test)

# Modelo

modelo_rlm = LinearRegression()

# Entrenamiento

metodo.entrenamiento(modelo_rlm, X_train, y_train)

y_hat = modelo_rlm.predict(X_test)
print(y_hat)

# Metricas

metodo.metricas_regresion(y_test, y_hat)

# Grafica

plt.scatter(y_test, y_hat)
plt.plot(y_test, y_test)

plt.show()