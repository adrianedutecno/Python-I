"""
Requerimos crear una variable con el número 8, una con el número 10.5, y una con la palabra “ejercicio”. 
Luego, crear un set que contendrá cada una de las variables que creamos, y será asignado a una variable.
A continuación, crearemos una lista que contendrá el set creado anteriormente, 
y una variable con el valor lógico False. 
Esta lista la asignaremos a una variable que luego imprimiremos en pantalla.
"""

#crear variables con el número 8, una con el número 10.5, y una con la palabra “ejercicio”
# #camelCase
# variableUno = 1
# variableDos = 2
# variableTres = 3

#snake_case
#identidicador = valor_asignado
variable_uno = 8
variable_dos = 10.5
variable_tres = "ejercicio"

#creacion de un set que contendrá cada una de las variables que creamos
# set()
# {}
#identificador = valor_asignado
# otro_set = set({variable_uno,variable_dos,variable_tres})
# tercer_set = set({}) #set vacio
# tercer_set.add(variable_uno)
# tercer_set.add(variable_dos)
# print(tercer_set)
un_set = {variable_uno, variable_dos, variable_tres}

#A continuación, crearemos una lista que contendrá el set creado anteriormente, 
#y una variable con el valor lógico False. 
una_lista = [un_set,False]

#Esta lista la asignaremos a una variable que luego imprimiremos en pantalla.
print(una_lista)


