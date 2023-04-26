"""
indique si es positivo o negativo, y si es par o impar. 
En caso de ser cero, también indicarlo.
"""

#Pedimos al usuario que introduzca un número
num = int(input("Introduce un número: "))

#Definimos un diccionario para asociar los valores pares y positivos a las etiquetas de salida
#asigna cada tupla de pares y positivos a una etiqueta que describe el número.
output_labels = {
    (0, 0): "El número es cero",
    (1, 0): "El número es positivo y par",
    (1, 1): "El número es positivo e impar",
    (-1, 0): "El número es negativo y par",
    (-1, 1): "El número es negativo e impar"
}

#Obtenemos los valores, si es par y si es positivo utilizando operaciones bit a bit
parity = num & 1  # 1 si es impar, 0 si es par
positivity = (num > 0) - (num < 0)  # 1 si es positivo, -1 si es negativo, 0 si es cero

#Obtenemos la etiqueta de salida del diccionario utilizando los valores pares y positivos
output_label = output_labels[(positivity, parity)]

# Imprimimos la etiqueta de salida
print(output_label)