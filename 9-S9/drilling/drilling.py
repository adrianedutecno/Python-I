"""
Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos
números, y otra que divida dos números. Adicionalmente, crear una función que acepte dos
números como parámetros y regrese el resultado en forma de tupla de su suma, resta,
multiplicación y división.
Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta,
Multiplicación y División, y los valores de cada clave serán los resultados obtenidos con la función
creada anteriormente.
"""

# Definir funcion Suma
def sumar(n1, n2):
    suma = n1 + n2
    return suma


# Definir funcion Resta
def restar(n1, n2):
    resta = n1 - n2
    return resta


# Definir funcion Multiplicación
def multiplicar(n1, n2):
    multi = n1 * n2
    return multi


# Definir funcion Division
def dividir(n1, n2):
    division = n1 // n2
    return division


# Definir Tupla
def tupla(n1, n2):
    resultado = tuple((sumar(n1, n2), restar(n1, n2), multiplicar(n1, n2), dividir(n1, n2)))
    # return (sumar(n1, n2), restar(n1, n2), multiplicar(n1, n2), dividir(n1, n2))
    return resultado


# V Tupla
result = tupla(4, 2)
print(result)

# Crear diccionario
diccionario = {
    "Suma": result[0],
    "Resta": result[1],
    "Multiplicacion": result[2],
    "División": result[3],
}

# Resultar resultados.
print(diccionario)