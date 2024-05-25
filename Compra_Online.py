
# Algoritmo de compra online

import sqlite3 as sqlite

# Conectar a la bbdd de ventas
bbdd = sqlite.connect("Datos_De_Venta.db")
cursor = bbdd.cursor()

# Obtener los productos
cursor.execute(f"SELECT * FROM Productos")
datos = cursor.fetchall()

internet = input("¿Hay internet?: ")

if internet.lower() == "si":

	print("\nProductos:\n")
	for i in range(0, len(datos)):
		print(datos[i])

	pregunta_comprar = input("\n¿Quieres comprar?: ")

	if pregunta_comprar.lower() == "si":
		comprar = input("¿Que quieres comprar? (Ingrese el nombre del producto): ")
		producto = comprar
		
		for i in range(0, len(datos)):
			if producto in datos[i]:
				cursor.execute(f"UPDATE Productos SET Cantidad = {datos[i][2] - 1} WHERE ID = {i + 1}")
				print("Obtendras tu producto")
else:
	print("No obtendras el elemento")

bbdd.commit()
bbdd.close()