#ciclo for
#se utiliza para el recorrido de datos, en listas, tuplas, diccionarios, set, String
#se utiliza el metodo range() para obtener el rango hasta donde se debe recorrer
#se utiliza el metodo len() para obtener el tamaño de la estructura que se recorre

#indice [0, 1, 2, 3, 4, 5] desde 0 a n-1 siendo n la cantidad de elementos
lista = [1, 2, 3, 4, 5, 6, 1] #lista con 6 elementos

#recorriendo o conociendo los elementos de la lista
contador = 0
for item in lista:
    print("Recorriendo el elemento de la lista ",item)
    if item == 1:
        contador += 1
        print("Existe el numero 1")
        
print(contador)
    
#recorriendo o conociendo el indice de la lista
for item in range(len(lista)):
    print("Recorriendo el indice de la lista ",item)
    print("Recorriendo el elemento de la lista ",lista[item])
    
#recorriendo o conociendo el indice de la lista
for item in lista:
    print("Recorriendo el indice de la lista ",lista.index(item))