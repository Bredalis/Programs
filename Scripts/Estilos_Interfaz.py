
<<<<<<< HEAD
=======
# Librerías

>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
import sqlite3 as sqlite
import pandas as pd

bbdd = sqlite.connect("../BBDD/Estilos_Interfaz.db")
cursor = bbdd.cursor()

cursor.execute(f"SELECT * FROM Estilos")
datos = cursor.fetchall()

<<<<<<< HEAD
letras = [datos[i][1] for i in range(0, len(datos))]
cursor = [datos[i][2] for i in range(0, len(datos))]

# Crear un df con esas listas
df_estilos = pd.DataFrame({
	"Letras": letras,
	"Cursor": cursor
})

print("Estilos de letras y cursores:\n\n", df_estilos)
=======
lista_letras = []
lista_cursor = []

# Pasar los datos a listas

for i in range(0, len(datos)):
	lista_letras.append(datos[i][1])
	lista_cursor.append(datos[i][2])

# Crear un df con esas listas

df_estilos = pd.DataFrame({
	"Letras": lista_letras,
	"Cursor": lista_cursor
})

print("\n", df_estilos) 
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da

bbdd.commit()
bbdd.close()