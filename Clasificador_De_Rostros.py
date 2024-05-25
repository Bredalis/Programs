
import  cv2
import winsound

color = (255, 0, 0)
grosor = 2

url = "haarcascade_frontalface_default.xml"
clasificador = cv2.CascadeClassifier(url)
captura_video = cv2.VideoCapture(0)

print("Clasificador de rostro")
nombres = ["lisa", "yulissa", "christopher"]
respuesta = input("Ingrese su nombre para clasificarlo: ")
respuesta = respuesta.split(",")
print("Por favor, pongase en el orden de los nombres ingresados")

while True:

	resultado, ventana = captura_video.read()
	ventana_gris = cv2.cvtColor(ventana, cv2.COLOR_BGR2GRAY)

	caras = clasificador.detectMultiScale(ventana_gris, minNeighbors = 5)

	for i, (x, y, ancho, alto) in enumerate(caras):

	    cv2.rectangle(ventana, (x, y), (x + ancho, y + alto), color, grosor)

	    # Agregar texto diferente para cada rostro

	    texto = respuesta[i] if respuesta[i] in nombres else f"No identificado"
	    cv2.putText(
	    	ventana, texto, (x, y - 10), 
	    	cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

	cv2.imshow("Video", ventana)

	if cv2.waitKey(1) == ord("x"):
		break

cv2.destroyAllWindows()
captura_video.release()