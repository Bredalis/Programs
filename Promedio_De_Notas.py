
# Promedio de 4 notas

def promedio(notas):
	
	if len(notas) != 4 or len(notas) < 4:
		print("Tiene que ingresar 4 notas")  

	else:
		promedio = sum(notas) / 4 
		print(promedio)

promedio([56, 70, 88, 68]) # Ingrese las notas aqui