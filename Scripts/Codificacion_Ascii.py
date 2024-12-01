
import tensorflow as tf

<<<<<<< HEAD
print("Codificar y decodificar ASCII")
def codificar(texto: str):
  try:
    texto = tf.io.decode_raw(tf.constant(texto), tf.uint8).numpy()
    return " ".join(str(letra) for letra in texto)
  except Exception as e:
    return f"Error inesperado: {e}"

def decodificar(texto: str):
  try:
    return "".join(chr(int(letra)) for letra in texto.split())
  except Exception as e:
    return f"Error inesperado: {e}"
=======
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
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
