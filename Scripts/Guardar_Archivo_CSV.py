
import csv

def crear_archivos(ruta, datos):
	ruta_archivo = ruta

	# Escribir los datos 
	# en el archivo

	with open(ruta_archivo, "w", newline = "") as archivo:
		escribir_csv = csv.writer(archivo)

		# Ingresar los datos
		escribir_csv.writerow(datos) 