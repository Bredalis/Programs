
# Diagrama de flujo automatizado

from py2flowchart import pyfile2flowchart

try:
	print("Programa que te crea diagramas de flujo a partir de tu script de Python")
	nombre_programa = input("Ingrese la ruta del programa: ")

	pyfile2flowchart(f"{nombre_programa}.py", f"../DiagramasDeFlujo/HTML/{nombre_programa}.html")
	print("¡Listo!")

except Exception as e:
	print(f"Error inesperado: {e}")