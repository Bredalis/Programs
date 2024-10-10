
# Algoritmo para determinar 
# si un número es primo o no

def numeros_primos():
    try:
        numero = int(input("Ingrese el numero: "))
        
        if numero <= 1:
            return f"{numero} no es primo"

        for i in range(2, numero):
            if numero % i == 0:
                return f"{numero} no es primo"
        
        return f"{numero} es primo"

    except ValueError:
        return "Solo numeros"