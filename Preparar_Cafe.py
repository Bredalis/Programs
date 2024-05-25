
# Algoritmo para 
# preparar cafe

pregunta = input("¿Quiere café?: ")
tipos_cafe = ["Negro", "Con leche", "Normal"]

if pregunta.lower() == "si":

	print("\nTipos de café:")
	for i in tipos_cafe:
		print("-", i)

	preferencia = input("\n¿Cómo lo quieres?: ")

	if preferencia == "Negro":
		print("Preparo el café y el agua")

	elif preferencia == "Con leche":
		print("Preparo,la leche, el café, la azúcar y el agua")

	else:
		print("Preparo el café, el agua y la azúcar")

	print("¡Café listo!")

else:
	print("Entonces no habra café")