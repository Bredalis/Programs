
<<<<<<< HEAD
# Diagrama de flujo automatizado

from py2flowchart import pyfile2flowchart

try:
	print("Programa que te crea diagramas de flujo a partir de tu script de Python")
	nombre_programa = input("Ingrese la ruta del programa: ")

	pyfile2flowchart(f"{nombre_programa}.py", f"../DiagramasDeFlujo/HTML/{nombre_programa}.html")
	print("¡Listo!")

except Exception as e:
	print(f"Error inesperado: {e}")
=======
# Diagramas de flujo automatizado

from py2flowchart import pyfile2flowchart

print("Programa que te crea diagramas de flujo a partir de tu script de Python")
programa_nombre = input("Ingrese el nombre del programa: ")

pyfile2flowchart(programa_nombre + ".py", "../DiagramasDeFlujo/HTML/" + programa_nombre + ".html")
print("Listo!")
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
