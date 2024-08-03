
# Promedio de 4 notas

def promedio(notas):
	
	if len(notas) != 4 or len(notas) < 4:
		return "Tiene que ingresar 4 notas" 

	promedio = sum(notas) / 4 
	return promedio

notas = [56, 70, 88, 88]
print(promedio(notas))