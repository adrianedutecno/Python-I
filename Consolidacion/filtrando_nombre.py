"""
Se tiene una lista de nombres de personas 
["Juan", "María", "Pedro", "Ana", "Roberto", "Lucía", "Luisa"]
Imprimir los nombres que tienen una longitud mayor que 5 caracteres. 
Puedes hacerlo utilizando un bucle for y una estructura de control if 
para filtrar los nombres.
"""

nombres = ["Juan", "María", "Pedro", "Ana", "Roberto", "Lucía", "Luisa"]

print("Los nombres con más de 5 caracteres son: ")
for nombre in nombres:
    if len(nombre) > 5:
        print(nombre)
