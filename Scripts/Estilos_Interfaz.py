
import sqlite3 as sqlite
import pandas as pd

bbdd = sqlite.connect("../BBDD/Estilos_Interfaz.db")
cursor = bbdd.cursor()

cursor.execute(f"SELECT * FROM Estilos")
datos = cursor.fetchall()

letras = [datos[i][1] for i in range(0, len(datos))]
cursor = [datos[i][2] for i in range(0, len(datos))]

# Crear un df con esas listas
df_estilos = pd.DataFrame({
	"Letras": letras,
	"Cursor": cursor
})

print("Estilos de letras y cursores:\n\n", df_estilos)

bbdd.commit()
bbdd.close()