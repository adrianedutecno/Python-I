"""
Crear una función que acepte 3 números como parámetros, sume todos los valores, y
adicionalmente reste el segundo y tercer parámetro al primero.
Al invocar la función, debemos pasarle los parámetros en forma de lista. Esta devolverá ambos
resultados en una tupla. Los resultados se deben imprimir en pantalla.
"""

# Funcion Suma
def suma(n1, n2, n3):
    # Suma de todos los valores
    suma_1 = n1 + n2 + n3
    # Resta del segundo y tercero por el primero
    suma_final = n1 - (n2 + n3)
    return (suma_1, suma_final)

# Funciona Suma (Alternativa)
def sumab(lista):
    # Suma de todos los valores
    suma_1 = lista[0] + lista[1] + lista[2]
    # Resta del segundo y tercero por el primero
    suma_final = lista[0] - (lista[1] + lista[2])
    return (suma_1, suma_final)

# Ingresar parametros como lista
lista = [1, 2, 3]
resultado = suma(*lista)

# Ciclo for para mostrar valor
a = 0
for n in resultado:
    a = a + 1
    print(f"Valor {a} : {n}")

# Entregar lista
print("Tupla:", suma(*lista))
print("Tupla V2:", sumab(lista))