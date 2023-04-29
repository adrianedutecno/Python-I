"""
Tuplas, son colecciones de datos, se puede acceder por el indice del elemento
Se definen con la funcion tuple()
Se definen con parentesis nombre_tupla = ()  
"""
#definir una tupla
tupla = tuple()
tupla = ()
num = 1, 2, 3, 4, 5, 6
print(tupla)
print(num)

#indice van desde 0 a n-1 siendo n la cantidad de elementos
#indices(0 ,   1,     2,          3)
tupla = (31,1.80,"Jose","Feliciano")
#se aceptan indices negativos para la tupla

#acceder al tipo de dato de la tuple
print("El tipo de dato de la tupla es: ",type(tupla)) #<class 'tuple'>

#acceder a los ementos de la tupla con los indices, nombre_tupla[indice]
print("El elemento en el indice 0 es: ",tupla[0])
print("El elemento en el indice -1 es: ",tupla[-1]) #indice negativo parte desde la ultima parte de la tupla, desde su ultimo elemento

#funciones de la tupla
#count(), index(indice)

#funcion count(elemento)
print("El elemento 31 su cuenta es:",tupla.count(31)) #1
print(f"El elemento 31 su cuenta es: {tupla.count(31)}") #1
print("El elemento 31 su cuenta es: {} {}".format(tupla.count(31),"VALOR AGREGADO")) #1

#funcion index(elemento)
indice_elemento = tupla.index("Feliciano")
print("El indice del elemento Feliciano es: ",indice_elemento)

#subtuplas extraer elementos de una tupla
# (31,1.80,"Jose","Feliciano")
sub_tupla = tupla[0:3]
print(sub_tupla)
print(tupla[1:3])

#No permiten eliminar elementos de una tupla
#tupla.remove(31) #AttributeError: 'tuple' object has no attribute 'remove'
#del tupla[2] #TypeError: 'tuple' object doesn't support item deletion