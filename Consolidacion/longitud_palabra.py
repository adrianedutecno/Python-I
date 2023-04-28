"""
Se tiene la siguiente lista ["gato", "perro", "elefante", "jirafa", "tigre"]
Crear una lista de números donde cada número es la longitud de una palabra.
"""
lista = ["gato", "perro", "elefante", "jirafa", "tigre"]

longitudes = []
for i in range(len(lista)):
    longitudes.append(len(lista[i]))
    
print(longitudes)

"""
"""
for i in lista:
    longitudes.append(len(i))
    
print(longitudes)