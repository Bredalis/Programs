
import tensorflow as tf

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