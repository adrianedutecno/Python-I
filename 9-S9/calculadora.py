"""
# Se pide realizar una calculadora declarando funciones para cada tipo de calculo que se realice
# realizar un menu con opciones para seleccionar que calculo se desea realizar
# el ingreso es por consola, requerir al usuario la opcion y numeros al que se realizara el calculo
-verificar errores de ingreso
# verificar division por cero
"""
#print(suma(2,1)) #funciones deben ser definidas antes de invocarlas, si estan en el mismo archivo
#def nombre_funcion(parametro1,parametro2):
def suma(num1, num2):
    sumatoria = num1 + num2
    return sumatoria

def resta(num1: float, num2: float):
    return num1 - num2 

def multiplicar(num1,num2) -> float:
    return num1 * num2

def dividir(num1,num2):
    if num2 == 0:
        return None
    else:
        return num1 / num2

def opciones_a_mostrar():
    print("Bienvenido a la Calculadora")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")
    print("Ingrese una Opcion: ")

#funcion calculadora, llevara el menu y realizara los calculos usando las funciones y estructuras condicionales
def calculadora():
    while True: #mientras sea True o no exista un break o return, se seguira ejecutando el ciclo
        try:
            #requerir y mostrar opciones al usuario
            opciones_a_mostrar() #invocando a la funcion para mostrar las opciones al usuario
            
            #ingresar los valores de opcion y numeros al que se realizara el calculo
            opcion = input("1/2/3/4/5: ")
            num1 = float(input("Ingrese el primer numero:"))
            num2 = float(input("Ingrese el segundo numero:"))
            #evaluar opcion y seleccionar una funcion a realizar si se cumple la condicion
            match opcion:
                case '1':
                    resultado = suma(num1,num2) #invocando a la funcion suma, que necesita dos parametros de ingreso
                case '2':
                    resultado = resta(num1,num2)
                case '3':
                    resultado = multiplicar(num1,num2)
                case '4':
                    resultado = dividir(num1,num2)
                case '5':
                    #return si es funcion
                    #break si es ciclo
                    print("Gracias por usar la calculadora vuelva pronto!!!")
                    break
                case _: 
                    #resultado = None
                    print("Opción no valida, elija una opción válida")
                    
            if resultado is not None:
                print(f"El resultado de el calculo entre {num1} y {num2} es: {resultado}")
                            
        except Exception as e: #si sucede algun error, se imprime en consola el error
            print("Error: ",e)               
    
calculadora() #invocando a la funcion calculadora
    
