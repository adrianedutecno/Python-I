"""
Set, coleccion de datos, conjunto de datos
Se define utilzando la funcion set()
se puede definir con {} pero se inicializa como un diccionario
"""
#Definir un set
set_datos = set({10,20,15,4,3,2})
my_set = {} #se inicializa como un diccionario

#verificar o ver el tipo de dato de un set
print("El tipo de dato de set_datos es:", type(set_datos)) #<class 'set'>
print("El tipo de dato de my_set es:", type(my_set)) #<class 'dict'>

#verificar el largo de un set, longitud con len(parametro)
print("Largo de set_datos es:", len(set_datos))
print("Largo de my_set es:", len(my_set))

#agregar elementos a un set
set_datos.add(1)
print("set_datos: ", set_datos)

my_set = set() #inicializando un set vacio
my_set.add(2)

#No permite elementos repetidos
set_datos.add(1)
print("set_datos: ", set_datos)

#busqueda de elementos en un set, elemento_buscado in set, retorta True or False
print("Busqueda del numero 10 en set_datos:", 10 in set_datos)
print("Busqueda del numero 10 en set_datos:", "Python" in set_datos)

#remover elementos de un set, remove(elemento), no acepta indice
set_datos.remove(15)
set_datos.add("String")
#set_datos.add("String","String2") #TypeError: set.add() takes exactly one argument (2 given)
set_datos.remove("String")
print("set_datos: ", set_datos)

#remover todos o borrar el set, limpiar
my_set.clear()
print("my_set: ", my_set)

del my_set #elimina el set, la variable my_set no existe
#print("my_set: ", my_set) #name 'my_set' is not defined

#actualizar un set, funcion update(set_a_agregar)
set_datos.update({3,12,11,25})
print("set_datos: ", set_datos)

#otras operaciones
#union() entrega un nuevo set de la union
my_set = {50,100,200}
new_set = set_datos.union(my_set)
print("new_set: ", new_set) #{1, 2, 3, 4, 100, 200, 10, 11, 12, 50, 20, 25}
print("imprimiento retorno del nuevo set: ", set_datos.union(my_set)) #{1, 2, 3, 4, 100, 200, 10, 11, 12, 50, 20, 25}

#interseccion() #datos existentes dentro de dos set, valores en común
interseccion_set = new_set.intersection(my_set)
print("interseccion_set: ", interseccion_set) #{200, 50, 100}

#difference(set_a_comparar), retorna un nuevo set con los datos diferentes entre los set
diferencias_set = new_set.difference(my_set) #{1, 2, 3, 4, 10, 11, 12, 20, 25}
print("difference:", diferencias_set)

#conversion
my_set = list(my_set)
set_datos = tuple(set_datos)
print("my_set convertido a una lista: ", my_set) #[200, 50, 100]
print("set_datos convertido a una tupla: ",set_datos) #(1, 2, 3, 4, 10, 11, 12, 20, 25)