
# Librerias

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from Metodos_Modelo import *

# Metodo

metodo = MetodosParaModelos()

# Obtener datos

url = "Dogs_And_Cats.csv"
df = pd.read_csv(url)

print(df)
print(df.shape)

print(df["animals"][1])

# Preprocesamiento 

lista_categorica = ["animals", "labels"]

# (One-Hot-Encoder)

for categorico in lista_categorica:

	transformacion = pd.get_dummies(df[categorico], 
		prefix = categorico, dtype = int, drop_first = True)

	df = df.join(transformacion)

df_categorico = df.columns.values.tolist()
columnas_limpias = [i for i in df_categorico if i not in lista_categorica]

df_limpio = df[columnas_limpias]
df_limpio.columns = ["animals", "labels"]

print(df_limpio)

# Dividir datos

X = df_limpio.iloc[:, df_limpio.columns == "animals"]
y = df_limpio.iloc[:, df_limpio.columns == "labels"]

print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,
	random_state = 99)

# Modelo

modelo_rl = LogisticRegression(max_iter = 10000)

# Entrenamiento

metodo.entrenamiento(modelo_rl, X_train, y_train)

# Sacar predicciones del modelo

y_pred = modelo_rl.predict(X_test)

# Aplicar metricas

metodo.metricas_clasificacion(y_pred, y_test)

y_test_lista = y_test.values.tolist()
y_test_limpia = []	

for i in range(0, len(y_test_lista)):
	y_test_limpia.append(y_test_lista[i][0])

print("\ny_test - y_pred")
for i in range(0, len(y_pred)):
	print(f"{y_test_limpia[i]} - {y_pred[i]}")