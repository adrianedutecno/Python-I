#set, coleccion de elementos y son unicos, no acepta valores repetidos
lista = [1,2,3] #lista
lista = set(lista) #declarando un set(elemento) set({1,2,3})
print(lista)
nombre_set = set({1,2,3,4,5,6,7,8,9,10,11})
set = {1,1,2,3}

print(set) #{1, 2, 3}

#metodos de set

#añadir .add(elemento)
set.add(4)
print(set)

#remover .remove(elemento)
set.remove(1)
print(set)

#interseccion de elementos
elementos_comunes = nombre_set.intersection(lista)
print(elementos_comunes)

#diferencia simetrica entre set
element_unicos = nombre_set.symmetric_difference(lista)
print(element_unicos)

#elementos diferentes
elementos_diferentes = nombre_set.difference(lista)
print(elementos_diferentes)