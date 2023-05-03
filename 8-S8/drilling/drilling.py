"""
Se solicita recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas: 1 [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
• Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
• Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
• Finalmente, imprimiremos en pantalla el diccionario resultante.
Ejemplo de impresión en pantalla:
"""

lista_de_listas = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]

diccionario = dict()
otro_diccionario = dict()
claves = ["A", "B", "C", "D"]

contador = 0 #conocer posicion de la lista para las claves y agregar elementos al diccionario

for element in lista_de_listas:
    #insertar nombre_diccionario[clave] = valor
    diccionario[claves[contador]] = element #diccionario[lista[indice]] = elemento_que_se_recorre
    otro_diccionario[claves[lista_de_listas.index(element)]] = element
    contador += 1
    if element[0] == 0:
        continue    
    for num in element:
        if num == 0:
            continue        
        print(num)
        
print(diccionario)
print(otro_diccionario)