#operadores logicos
#and or not
#evaluar bool o booleanos True or False
a = True
b = False

print(a and b) #False, deben cumplirse las dos condiciones
print(a or b) #True, debe cumplirse alguna de las condiciones
print(not a) #False, not cambia el valor de la condicion
print(not (a or b)) #False
print(not (a and b)) #True
print("-----------------------------------")

#operadores de comparacion
#comparacion de numeros, tamaños, verificar contadores o iteradores
c = 10
d = 5

print(c < d) #False, menor que
print(c > d) #True, mayor que
#print(a > b) #True
#print(a < b) #False
print(c <= d) #False, menor igual que
print(c >= d) #True, mayor igual que
print(c == d) #False, igual que
print(c != d) #True, distinto que