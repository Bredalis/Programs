
# Definimos dos conjuntos con números
conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {4, 5, 6, 7, 8}

# Unión: todos los elementos de ambos conjuntos (sin duplicados)
union = conjunto_A.union(conjunto_B)
print("Unión de A y B:", union)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersección: elementos comunes en ambos conjuntos
interseccion = conjunto_A.intersection(conjunto_B)
print("Intersección de A y B:", interseccion)  # {4, 5}

# Diferencia: elementos de A que no están en B
diferencia = conjunto_A.difference(conjunto_B)
print("Diferencia de A y B:", diferencia)  # {1, 2, 3}

# Diferencia simétrica: elementos que están en A o B, pero no en ambos
diferencia_simetrica = conjunto_A.symmetric_difference(conjunto_B)
print("Diferencia simétrica de A y B:", diferencia_simetrica)  # {1, 2, 3, 6, 7, 8}