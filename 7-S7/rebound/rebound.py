"""
Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for, 
e imprimir en pantalla el valor de cada elemento indicando si es par, impar o cero.
"""
digitos = [0,1,5,100,3,33,56,17,98,61]

for i in digitos:
    if i == 0:
        print("El numero es 0.")
    elif i % 2 == 0 :
        print(f"El numero {i} es par.")
    else:
        print(f"El numero {i} es impar.")