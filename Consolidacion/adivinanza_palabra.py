"""
simula un programa que permite a los usuarios adivinar una palabra secreta:
"""

# palabra_secreta = "elefante"
# adivinanza = ""
# intentos = 0
# max_intentos = 5

# print("¡Bienvenido al juego de adivinanza de palabras!")
# print("Adivina la palabra secreta. Solo tienes", max_intentos, "intentos.")

# while adivinanza != palabra_secreta and intentos < max_intentos:
#     adivinanza = input("Ingresa tu adivinanza: ")
#     intentos += 1

#     if adivinanza == palabra_secreta:
#         print("¡Felicitaciones! Adivinaste la palabra secreta en", intentos, "intentos.")
#     elif intentos == max_intentos:
#         print("Lo siento, no tienes más intentos. La palabra secreta era", palabra_secreta)
#     else:
#         print("Tu adivinanza es incorrecta. Intenta nuevamente.")
        
"""

"""

import random
#funcion para adivinar palabra
def adivinanza_palabra(palabra_secreta,max_intentos):
    adivinanza = ""
    intentos = 0
    while adivinanza != palabra_secreta and intentos < max_intentos:
        adivinanza = input("Ingresa tu adivinanza: ")
        intentos += 1

        if adivinanza == palabra_secreta:
            print("¡Felicitaciones! Adivinaste la palabra secreta en", intentos, "intentos.")
        elif intentos == max_intentos:
            print("Lo siento, no tienes más intentos. La palabra secreta era", palabra_secreta)
        else:
            print("Tu adivinanza es incorrecta. Intenta nuevamente.")
            
#funcion para obtener una palabra random o secreta para el juego            
def obtener_palabra_random(lista_palabras):
    palabra_secreta = random.choice(lista_palabras)
    return palabra_secreta

            
#comienzo del objetivo del ejercicio
palabras = ['elefante', 'guitarra', 'computadora', 'helado', 'avion']

palabra_secreta = obtener_palabra_random(palabras)#invocando a la funcion obtener_palabra_random
max_intentos = 5

print("¡Bienvenido al juego de adivinanza de palabras!")
print("Adivina la palabra secreta. Solo tienes", max_intentos, "intentos.")

adivinanza_palabra(palabra_secreta,max_intentos)#invocacion a la funcion adivinanza_palabra
    

# while adivinanza != palabra_secreta and intentos < max_intentos:
#     adivinanza = input("Ingresa tu adivinanza: ")
#     intentos += 1

#     if adivinanza == palabra_secreta:
#         print("¡Felicitaciones! Adivinaste la palabra secreta en", intentos, "intentos.")
#     elif intentos == max_intentos:
#         print("Lo siento, no tienes más intentos. La palabra secreta era", palabra_secreta)
#     else:
#         print("Tu adivinanza es incorrecta. Intenta nuevamente.")