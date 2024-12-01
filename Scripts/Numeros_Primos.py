
# Algoritmo para determinar 
# si un número es primo o no

def numeros_primos():
    try:
        numero = int(input("Ingrese el número: "))
        
        if numero < 1:
            return "No es primo"

        for i in range(2, numero):
            return "No es primo" if numero % i == 0 else "Es primo"

    except ValueError:
        return "Error: Solo números"

    except Exception as e:
        print(f"Error inesperado: {e}")