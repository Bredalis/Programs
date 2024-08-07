
# Diagramas de flujo automatizado

from py2flowchart import pyfile2flowchart

print("Programa que te crea diagramas de flujo a partir de tu script de Python")
programa_nombre = input("Ingrese el nombre del programa: ")

pyfile2flowchart(programa_nombre + ".py", "../DiagramasDeFlujo/HTML/" + programa_nombre + ".html")
print("Listo!")