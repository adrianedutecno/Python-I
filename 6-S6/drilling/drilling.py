"""
Se requiere contar con un programa que, dados 3 números diferentes, 
los evalúe y entregue el orden de mayor a menor.
"""
num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercer número: "))

if len(set({num_1,num_2,num_3})) != 3:
    print("Debe ingresar numeros diferentes")
else:
    ordenados = sorted([num_1,num_2,num_3], reverse=True)
    print(ordenados)