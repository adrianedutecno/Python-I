"""
Carlcular la resistencia total dado el ingreso por consola
"""

# leer valores de entrada por consola
r1 = float(input("Resistencia 1: "))
r2 = float(input("Resistencia 2: "))
r3 = float(input("Resistencia 3: "))

# calcular la resistencia total
rt = 1/((1/r1) + (1/r2) + (1/r3))

# imprimir la resistencia total en consola
print("La resistencia total es de", rt)

"""
validar el ingreso de la resistencia, que sea mayor que 0, controlar error, y utilizar funciones
"""
#funcion para validar el ingreso de la resistencia en float
def validate_input_float(texto):
#ingreso de valores
    while True:
        try:    
            r = float(input(texto)) #float(), str(), int() casteo o transformacion, conversion del tipo de dato
            if r > 0:
                abs(r)
                return r
            else:
                print("El valor es menor a 0")
        except Exception as error:
            print("Ha ocurrido un error en el ingreso de la resistencia ",error)
            print("Ha ocurrido un error, ingrese de nuevo el valor de la resistencia")      
        
r_1 = validate_input_float("Ingrese la resistencia 1: ") ##lamada a funcion o invocando
r_2 = validate_input_float("Ingrese la resistencia 2: ")
r_3 = validate_input_float("Ingrese la resistencia 3: ")

# calcular la resistencia total
resistencia_total = 1/((1/r_1) + (1/r_2) + (1/r_3))

# imprimir la resistencia total en consola
print("La resistencia total es de", resistencia_total)

#Pedir cuantas resistencias se desean ingresar para calcular la resistencia total
#llamar al metodo validate_input_float las veces sea necesario con un ciclo
#acumular los valores de la resistencias e imprimir la resistencia total en consola