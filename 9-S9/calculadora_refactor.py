"""
# Se pide realizar una calculadora declarando funciones para cada tipo de calculo que se realice
# realizar un menu con opciones para seleccionar que calculo se desea realizar
# el ingreso es por consola, requerir al usuario la opcion y numeros al que se realizara el calculo
# verificar errores de ingreso
# verificar division por cero
"""
import os

#print(suma(2,1)) #funciones deben ser definidas antes de invocarlas, si estan en el mismo archivo
#def nombre_funcion(parametro1,parametro2):
def suma(numero1, numero2):
    sumatoria = numero1 + numero2
    return [sumatoria,numero1,numero2]

def resta(numero1: float, numero2: float):
    resta = numero1 - numero2
    return [resta,numero1,numero2] 

def multiplicar(numero1,numero2) -> float:
    multi = numero1 * numero2
    return [multi,numero1,numero2]

def dividir(numero1,numero2):
    if numero2 == 0:
        return None
    else:
        division = numero1 / numero2
        return [division,numero1,numero2]

def opciones_a_mostrar():
    print("Bienvenido a la Calculadora")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")
    print("Ingrese una Opcion: ")
    
def ingreso(texto):
    num = float(input(texto))
    return num

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#funcion calculadora, llevara el menu y realizara los calculos usando las funciones y estructuras condicionales
def calculadora():
    while True: #mientras sea True o no exista un break o return, se seguira ejecutando el ciclo
        try:
            clear_console()
            #requerir y mostrar opciones al usuario
            opciones_a_mostrar() #invocando a la funcion para mostrar las opciones al usuario
            
            #ingresar los valores de opcion y numeros al que se realizara el calculo
            opcion = input("1/2/3/4/5: ")
            mensaje = "Ingrese número:"
            #evaluar opcion y seleccionar una funcion a realizar si se cumple la condicion
            match opcion:
                case '1':
                    resultado = suma(ingreso(mensaje),ingreso(mensaje)) #invocando a la funcion suma, que necesita dos parametros de ingreso
                case '2':
                    resultado = resta(ingreso(mensaje),ingreso(mensaje))
                case '3':
                    resultado = multiplicar(ingreso(mensaje),ingreso(mensaje))
                case '4':
                    resultado = dividir(ingreso(mensaje),ingreso(mensaje))
                case '5':
                    #return si es funcion
                    #break si es ciclo
                    print("Gracias por usar la calculadora vuelva pronto!!!")
                    break
                case _: 
                    resultado = None
                    print("Opción no valida, elija una opción válida")
                    
            if resultado is not None:
                print(f"El resultado de el calculo entre {resultado[1]} y {resultado[2]} es: {resultado[0]}")
                            
        except Exception as e: #si sucede algun error, se imprime en consola el error
            print("Error: ",e)               
    
calculadora() #invocando a la funcion calculadora

# raise ZeroDivisionError("Cannot divide by zero"): generar una excepción de tipo ZeroDivisionError
# Exception: Clase base para todas las excepciones definidas en Python.
# AttributeError: Se produce cuando un objeto no tiene un atributo válido.
# TypeError: Se produce cuando se utiliza un tipo de dato incorrecto o inapropiado.
# ValueError: Se produce cuando se pasa un argumento con un valor inapropiado.
# NameError: Se produce cuando se utiliza un nombre que no está definido en el contexto actual.
# IndexError: Se produce cuando se intenta acceder a un índice de lista fuera de rango.
# KeyError: Se produce cuando se intenta acceder a una clave de diccionario que no existe.
# ZeroDivisionError: Se produce cuando se intenta dividir un número por cero.
# FileNotFoundError: Se produce cuando un archivo no puede ser encontrado.
# IOError: Se produce cuando hay un problema de entrada/salida en un archivo o en la consola.
# KeyboardInterrupt: Se produce cuando el usuario interrumpe la ejecución del programa (presionando Ctrl + C en la consola).
# StopIteration: Se produce cuando el método next() de un iterador no tiene más elementos para devolver.
    
