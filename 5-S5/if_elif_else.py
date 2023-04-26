#estructuras condicionales, para evaluar cierta condicion declarada o varias
#ingreso de valores por consola, se realiza mediante el metodo input

# num = int(input("Ingrese un número entero: "))
print("Ingrese un número entero")
num = input()
num = int(num)
#if(condicion), donde condicion siempre es True, al menos que se cambie o modifique
if(num > 0):
    print(f"El numero {num} es mayor a 0")
elif(num == 0):
    print(f"El numero {num} es igual a 0")
else:
    print(f"El numero {num} es menor a 0")
    
print("--------------------------------")
#uso de condicionales sin parentisis ()
if num > 0:
    print(f"El numero {num} es mayor a 0")
elif num == 0:
    print(f"El numero {num} es igual a 0")
else:
    print(f"El numero {num} es menor a 0")
