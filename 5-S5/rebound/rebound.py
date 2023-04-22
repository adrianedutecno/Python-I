"""
Requerimos calcular el factorial de un número, asignarlo a una variable, y luego imprimirla. 
Sabiendo que el factorial es el resultado de la multiplicación de todos los enteros positivos que hay entre un número y uno. 
Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1.
"""
#variable que acumule el valor ingresado por el usuario
num = 0

#ciclo para pedir el ingreso del numero y que sea positivo
while True:
    num = int(input("Ingrese un número entero positivo: "))
    if num > 0: #si el numero es mayor a 0
        break
    
#factorial es el resultado de la multiplicación de todos los enteros positivos
#que hay entre un número y uno.
#ejemplo 4 multiplicado por cada numero = 4 * 1, 2, 3, 4,
factorial = 1
i = 1
while True:
    factorial *= i #acumulando el factorial por cada valor del iterador
    i += 1 #cambiando el valor del iterador
    if i > num:
        break
    
print(f"El factorial de {num} es {factorial}")