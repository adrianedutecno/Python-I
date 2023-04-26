"""
menu utilizando match case
"""

while True:
    opcion = int(input("Hola, bienvenido\n " 
                       "1.- Saludar\n " 
                       "2.- preguntar que hay en la tele\n " 
                       "3.- que opinas de la música que escucho?\n" 
                       "4.- que estás sintiendo ahora?\n" 
                       "5.- Salir\n\n" 
                       "Ingresa una opción => ")
                 )
    
    match opcion: 
        case 1: 
            print("Hola, que tal?") 
        case 2: 
            print("No hay nada bueno") 
        case 3: 
            print("Es buena música") 
        case 4: 
            print("Tengo hambre!") 
        case 5: 
            print("Nos vemos!") 
            break 
        case _: 
            print("Esa opcion no es válida!")
