#estructuras condicionales, para evaluar cierta condicion declarada o varias
#ingreso de valores por consola, se realiza mediante el metodo input

# numero = int(input("Ingrese un número entero: "))
print("Ingrese un número entero")
numero = input()
numero = int(numero)
#if(condicion), donde condicion siempre es True, al menos que se cambie o modifique
if(numero > 0):
    print(f"El numero {numero} es mayor a 0")
elif(numero == 0):
    print(f"El numero {numero} es igual a 0")
else:
    print(f"El numero {numero} es menor a 0")
    
print("--------------------------------")
if numero > 0:
    print(f"El numero {numero} es mayor a 0")
elif numero == 0:
    print(f"El numero {numero} es igual a 0")
else:
    print(f"El numero {numero} es menor a 0")
