"""
Tienes la siguiente lista de números:
[45, 23, 67, 89, 12, 56, 78, 90, 90]
Encontrar el número más grande en la lista utilizando un bucle for
"""

lista = [45, 23, 67, 99, 12, 356, 78, 90] 
mayor = lista[-1] 
menor = lista[0]
repetido = 0
for elemento in lista: 
    if elemento > mayor: 
        mayor = elemento
    if elemento < menor:
        menor = elemento
        
print(mayor)
print(menor)