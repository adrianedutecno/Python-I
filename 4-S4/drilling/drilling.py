"""
Requerimos crear un registro de datos personales de tres personas. 
Los datos que se necesitan son: su nombre, apellido y teléfono. 
Para ello, generaremos un diccionario para cada una de las personas con los datos mencionados, 
y luego los almacenaremos dentro de una lista. Finalmente, imprimiremos en pantalla la lista.
"""
#los diccionarios, colecciones de datos formados por clave y valor
persona_uno = {'nombre': 'Juan', 'apellido': 'Perez', 'telefono': 123456789}
persona_dos = {
    'nombre': 'Maria', 
    'apellido': 'Fernandez',  
    'telefono': 123456789
    }
persona_tres = {"nombre": "Fulanito", "apellido": "Gonzales", "telefono": 123456789}

lista_uno = [persona_uno, persona_dos, persona_tres]
print(lista_uno)

# diccionario = {}
# diccionario.update(persona_uno)
# print(diccionario)

#-----------------------------------------------------------------------------
personas = {
    "persona_uno" : {'nombre': 'Juan', 'apellido': 'Perez', 'telefono': 123456789},
    "persona_dos" : {
    'nombre': 'Maria', 
    'apellido': 'Fernandez',  
    'telefono': 123456789
    },
    "persona_tres" : {"nombre": "Fulanito", "apellido": "Gonzales", "telefono": 123456789},
    "persona_cuatro" : {
        "nombre": "Fulanito", 
        "apellido": "Gonzales", 
        "telefono": 123456789,
        "direccion": {
            "calle": "Calle 123",
            "region": "Región IV"
            }
        }
}

print(personas["persona_uno"]["nombre"])
print(personas["persona_cuatro"]["direccion"]["calle"])
print(personas["persona_cuatro"]["direccion"]["region"])