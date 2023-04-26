"""
Se requiere contar con un programa que, dados 3 números diferentes, 
los evalúe y entregue el orden de mayor a menor.
"""
num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercer número: "))

#(set) con los valores de num_1, num_2 y num_3, admite solo elementos únicos
#si alguno de los valores se repite, el conjunto tendrá menos de 3 elementos 
if len(set({num_1,num_2,num_3})) != 3: #len para obtener la longitud del conjunto.
    #si es diferente de 3, significa que al menos uno de los números se repite, no son diferentes.
    print("Debe ingresar numeros diferentes")
else:
    ordenados = sorted([num_1,num_2,num_3], reverse=True)
    print(ordenados)