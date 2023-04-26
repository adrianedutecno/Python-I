'''
simulación de una bomba de tiempo. Al ejecutar el programa, se imprimirá el mensaje "Bomba del tiempo a explotar" 
'''

import time #importamos la librería de tiempo
print("Bomba del tiempo a explotar")
i = 5 #inicializamos la variable i como iterador en 5, va a ir decrementando en 1

while i >= 0: #mientras i sea mayor a 0
    print(i) #imprimimos el valor de i
    i -= 1 #decrementamos i en 1
    time.sleep(1) #tiempo de espera de 1 segundo

print("Boom ***")
