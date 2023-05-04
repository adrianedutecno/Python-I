"""
Se solicita crear un programa en Python que permita llevar el registro 
de los libros que han sido prestados por una biblioteca. 
Para ello, se pide crear un conjunto (set) con los nombres de los libros 
prestados.

A continuación, se solicita imprimir en pantalla la cantidad total de libros
prestados.

Finalmente, se debe crear otro conjunto con los nombres de los libros 
que han sido devueltos y mostrar en pantalla los libros que aún no han sido
devueltos. 

libros_prestados = {'Cien años de soledad', 'El amor en los tiempos del cólera', 'La ciudad y los perros', 'La casa verde', 'El otoño del patriarca', 'Rayuela', 'Pedro Páramo', 'La tregua'}
"""
#set de libros prestados
libros_prestados = {'Cien años de soledad', 'El amor en los tiempos del cólera', 'La ciudad y los perros', 'La casa verde', 'El otoño del patriarca', 'Rayuela', 'Pedro Páramo', 'La tregua'}

#cantidad total de libros prestados utilizando len()
print("La cantidad total de libros prestados es: ", len(libros_prestados))

#crear otro conjunto con los nombres de los libros que han sido devueltos
libros_devueltos = {'Cien años de soledad', 'La casa verde', 'La ciudad y los perros'}

#mostrar en pantalla los libros que aún no han sido devueltos

#difference() retorna un set con los nombres o datos diferentes entre los set
#buscar las diferencias del set más largo, si no se sabe cual es el mas grande utilizar ^
libros_sin_devolver = libros_prestados.difference(libros_devueltos) 
print("libros_sin_devolver:", libros_sin_devolver)

libros_sin_devolver = libros_devueltos.symmetric_difference(libros_prestados) #contraparte, usar el simbolo ^
print("libros_sin_devolver:", libros_sin_devolver)

libros_sin_devolver = libros_prestados ^ libros_devueltos #substraccion, contraparte usar la funcion set_uno.symmetric_difference(set_dos)
print("libros_sin_devolver:",libros_sin_devolver)

#buscar las diferencias del set más largo, si no se sabe cual es el mas grande utilizar ^
print("libros_sin_devolver:",libros_sin_devolver)
libros_sin_devolver = libros_devueltos - libros_prestados