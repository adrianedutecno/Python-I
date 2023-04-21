#ordenados por clave y valor
#diccionarios, es una coleccion de elementos
#declaracion con llaves {} o con la funcion dict()

estudiantes = {
    #clave:valor
    "Fulanito":25,
    "Maria": 22,
    "Jose": 40,
    "Marta": 30
}

print(estudiantes) #{'Fulanito': 25, 'Maria': 22, 'Jose': 40, 'Marta': 30}

#acceder al valor de una clave
# nombre_diccionario["clave"]
print(estudiantes["Fulanito"]) #25

#remover clave de un dicccionario
del estudiantes["Fulanito"]
print(estudiantes) #{'Maria': 22, 'Jose': 40, 'Marta': 30}

#obtener todas las claves de un dicccionario
claves = estudiantes.keys() 
print(claves) #dict_keys(['Maria', 'Jose', 'Marta'])

#obtener todos los valores
valores = estudiantes.values()
print(valores) #dict_values([22, 40, 30])

#borrar un diccionario
estudiantes.clear()
print(estudiantes)
