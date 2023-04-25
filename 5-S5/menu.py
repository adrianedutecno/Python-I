"""
Realizar la ejecución de un menú utilizando el lenguaje Python, 
donde se le indiquen varias opciones a seleccionar por el usuario 
y una opción para salir del menú.
Utilizar ciclos y estructuras condicionales.
"""
#importar libreria para expresiones regulares
import re
opcion = ""
patron = re.compile("^[1-5]{1}$") #compilacion de patron
while opcion != "5": #while True :
    #impresion del menu
    print("Hola, bienvenido, menú")
    print("1.- Opcion 1")
    print("2.- Opcion 2")
    print("3.- Opcion 3")
    print("4.- Opcion 4")
    print("5.- Salir del menú")
    print("Ingrese una opción")
    
    opcion = input() #leyendo la opción
    if re.match(patron,opcion):
        if opcion == "1":
            print("Realizando la opción 1")
        elif opcion == "2":
            print("Realizando la opción 2")
        elif opcion == "3":
            print("Realizando la opción 3")
        elif opcion == "4":
            print("Realizando la opción 4")
        elif opcion == "5":
            print("Saliendo, hasta luego")
            #break
        else :
            print("Ha ingresado una opción invalida, por favor ingrese una opción")
    else:
        print("Ha ingresado una opcion incorrecta, valide el ingreso")

"""
"""        
# while True: #while True :
#     #impresion del menu
#     print("Hola, bienvenido, menú")
#     print("1.- Opcion 1")
#     print("2.- Opcion 2")
#     print("3.- Opcion 3")
#     print("4.- Opcion 4")
#     print("5.- Salir del menú")
#     print("Ingrese una opción")
    
#     opcion = input() #leyendo la opción
#     if opcion == "1":
#         print("Realizando la opción 1")
#     elif opcion == "2":
#         print("Realizando la opción 2")
#     elif opcion == "3":
#         print("Realizando la opción 3")
#     elif opcion == "4":
#         print("Realizando la opción 4")
#     elif opcion == "5":
#         print("Saliendo, hasta luego")
#         break
#     else:
#         print("Ha ingresado una opción invalida, por favor ingrese una opción")