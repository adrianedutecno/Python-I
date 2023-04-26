# leer valores de entrada por consola
r1 = float(input("Resistencia 1: "))
r2 = float(input("Resistencia 2: "))
r3 = float(input("Resistencia 3: "))

# calcular la resistencia total
rt = 1/((1/r1) + (1/r2) + (1/r3))

# imprimir la resistencia total en consola
print("La resistencia total es de", rt)