
import tensorflow as tf

texto = input("Ingresa el mensaje para codificar: ")

def codificar():
  global texto
  texto = tf.io.decode_raw(tf.constant(texto), tf.uint8).numpy()

  for i in texto:
    print(i, end = " ")

def decodificar():

  for valor in texto:
    print(chr(valor), end = "")

codificar()
decodificar()