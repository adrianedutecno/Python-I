"""
Dada la siguiente lista de nombres:
• Harry Houdini
• Newton
• David Blaine
• Hawking
• Messi
• Teller
• Einstein
• Pele
• Juanes
Y sabiendo que Harry Houdini, David Blaine y Teller son magos. 
Y también que Newton, Hawking y Einstein son científicos. 
Debemos separar los nombres en tres grupos: magos, científicos y otros; 
y escribir una función llamada hacer_grandioso(), 
que modifique la lista de magos añadiendo la frase ‘El gran‘ antes del nombre de cada mago. 
Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la lista.
Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; 
luego imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.
"""
# Crear funcion hacer_grandioso() para modificar la lista de magos
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = 'el gran ' + magos[i]

# Definiendo una lista vacia para entregar valores
# def hacer_grandioso(magos):
#     grandiosos = []
#     for i in magos:
#         i = 'el gran ' + i
#         grandiosos.append(i)
#     return grandiosos

# Crear funcion imprimr_nombres()
def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

# Crear funcion para crear lista nueva
def crear_listas(magos, cientificos, otros, nombres):
    for nombre in nombres:
        if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
            magos.append(nombre)
        elif nombre in ['Newton', 'Hawking', 'Einstein']:
            cientificos.append(nombre)
        else:
            otros.append(nombre)


# Definimos lista de nombres
nombres = ['Harry Houdini', 'Newton', 'David Blaine',
           'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

# Creamos 3 grupos diferentes para cada nombre
magos = []
cientificos = []
otros = []

crear_listas(magos, cientificos, otros, nombres)

diccionario = {'magos': magos,
               'cientificos': cientificos,
               'otros': otros,
               'nombres': nombres}

# print(diccionario)

# # imprimimos la lista completa de personajes
print('lista completa de personajes: ')
imprimir_nombres(nombres)

# Modificando lista de magos
print('===================================================')
hacer_grandioso(magos)
imprimir_nombres(magos)

# imprimir cientificos
print('===================================================')
imprimir_nombres(cientificos)

# imprimir otros
print('===================================================')
imprimir_nombres(otros)
