
# Algoritmo para determinar 
# si un número es primo o no

def numeros_primos():
    try:
<<<<<<< HEAD
        numero = int(input("Ingrese el número: "))
        
        if numero < 1:
            return "No es primo"

        for i in range(2, numero):
            return "No es primo" if numero % i == 0 else "Es primo"

    except ValueError:
        return "Error: Solo números"

    except Exception as e:
        print(f"Error inesperado: {e}")
=======
        numero = int(input("Ingrese el numero: "))
        
        if numero <= 1:
            return f"{numero} no es primo"

        for i in range(2, numero):
            if numero % i == 0:
                return f"{numero} no es primo"
        
        return f"{numero} es primo"

    except ValueError:
        return "Solo numeros"
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
