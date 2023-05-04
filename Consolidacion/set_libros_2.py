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

while True:
    opciones = input('''que quieres hacer?    
                     Consultar libros prestados (c)    
                     Agregar libros devuetos (a)    
                     Salir (s)    ''').lower().strip()
    
    libros_prestados = {'Cien afios de soledad', 'El amor en los tiempos del c61era', 'La ciudad y los perros',
                        'La casa verde', 'El otoöo del patriarca', 'Rayuela', 'Pedro Påramo', 'La tregua'}
    libros_devueltos = {"caperucita roja", 'Python Machine Learning'}
    base_actualizada = libros_devueltos.symmetric_difference(libros_prestados)
    match opciones:
        case "c" | "consultar":
            print(f'La cantidad de libros prestados son {len(libros_prestados)}')
            print(f'Falta por devolver {base_actualizada}')
        case "a" | "agregar":
            libro_dev = input('Ingresa el libro ')
            libros_devueltos.add(libro_dev)
            print(f' Los libros devueltos son {libros_devueltos}')
        case "s" | "salir":
            print("Adios")
            break