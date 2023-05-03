"""
Diccionarios, colecciones estructuradas en clave:valor
clave como key
valor como value
Van estructurados entre llaves {} como un objeto JSON
Se puede definir usando dict()
Se puede definir usando {} llaves
"""
#creando un diccionario o instanciando un diccionario
my_dict = dict()
other_dict = {}

#se puede saber el tipo con type()
print("El tipo de diccionario es: ", type(my_dict))

other_dict = {
    #clave:valor
    'Nombre': 'Maria',
    'Apellido': 'Perez',
    'Edad': 25,
    'Direccion': 'Curico 1320'
}

my_dict = {
    #clave:valor
    'Nombre': 'Maria',
    'Apellido': 'Perez',
    'Edad': 25,
    'Direccion': {
        'Region': 'IV region',
        'Calle': 'Almirante Pastene',
        'Numero': '1320',
        'Codigo Postal': '123456789'
    }
}

print("other_dict: ", other_dict)
print("my_dict: ", my_dict)

#busqueda mediante una clave, nombre_diccionario[clave]
print("Nombre: ", my_dict['Nombre'])
print("Accediendo al numero de la clave direccion: ", my_dict['Direccion']['Numero']) #con notacion de corchetes
#print("Nombre: ", my_dict['nombre']) #KeyError: 'nombre' respeta las mayusculas para la busqueda de la clave

print("Apellido se encuentra dentro del diccionario my_dict: ", 'Apellido' in my_dict) #retorna True or False si existe o no la clave
print("EL valor 'Perez' dentro del diccionario mediante una clave: ",'Perez' in my_dict['Apellido'])

#actualizar algunn valor dada una clave
my_dict["Nombre"] = "Karla"
print("my_dict: ", my_dict)
my_dict['Direccion']['Numero'] = '1234'
print("my_dict: ", my_dict)

#insertar 
my_dict['Telefono'] = 956000876
print("Elemento Telefono insertado dentro del diccionario my_dict: ", my_dict)

#eliminar elemento dentro de un diccionario, del nombre_diccionario[clave]
print("other_dict: ", other_dict)
del other_dict['Edad']
print("other_dict: ", other_dict)

#funciones de los diccionarios

#items() entrega una tupla o arreglo de tuplas que incluyen clave y valor
print("utilizando la funcion items() en my_dict: ", my_dict.items())
#values()
print("utilizando la funcion values() en my_dict: ", my_dict.values())
#keys
print("utilizando la funcion keys() en my_dict: ", my_dict.keys())

#crea un nuevo diccionario con las claves y valores en None
diccionario = dict.fromkeys(my_dict)
print(diccionario)

#crea un nuevo diccionario dadas las claves en una tupla
otro_diccionario = dict.fromkeys(("Persona1","Persona2","Persona3"))
print(otro_diccionario)

