
print("Codificar y decodificar ASCII")

def codificar(texto: str):
  try:

    # Convierte cada caracter en su valor ASCII
    return " ".join(str(ord(letra)) for letra in texto)
  except Exception as e:
    return f"Error inesperado: {e}"

def decodificar(texto: str):
  try:
    # Convierte cada número en caracter ASCII
    return "".join(chr(int(letra)) for letra in texto.split())
  except Exception as e:
    return f"Error inesperado: {e}"