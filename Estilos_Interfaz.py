
# Librerias

import sqlite3 as sqlite
import pandas as pd

bbdd = sqlite.connect("Estilos_Interfaz.db")
cursor = bbdd.cursor()

cursor.execute(f"SELECT * FROM Estilos")
datos = cursor.fetchall()

lista_letras = []
lista_cursor = []

# Pasar los datos a listas

for i in range(0, len(datos)):
	lista_letras.append(datos[i][1])
	lista_cursor.append(datos[i][2])

print(lista_letras)
print(lista_cursor)

# Crear un df con esas listas

df_estilos = pd.DataFrame({
	"Letras": lista_letras,
	"Cursor": lista_cursor
})

print("\n", df_estilos) 

bbdd.commit()
bbdd.close()