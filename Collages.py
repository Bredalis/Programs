
"""
Collage de 4 imagenes. Aun necesita 
mantenimiento para agregarle la funcionalidad 
de graficar mas imagenes 
"""

import cv2	

# Obtener archivo StackImages

stackimages = open("StackImages.py", "r").read()
exec(stackimages)

def creacion_collage(url_1, url_2, url_3, url_4, ancho, alto):

	print("No puede graficar mas de 4 imagenes, por favor llenar todos los parametros")

	# Leer imagenes

	url_1 = cv2.imread(url_1)
	url_2 = cv2.imread(url_2)
	url_3 = cv2.imread(url_3)
	url_4 = cv2.imread(url_4)

	# Aplicando funcion de collage 

	img = stack_images(0.7, ([url_1, url_2], [url_3, url_4]))

	# Tamaño de la imagen

	img = cv2.resize(img, (ancho, alto))

	# Mostrar imagen
	
	cv2.imshow("Collage", img)
	cv2.waitKey(0)