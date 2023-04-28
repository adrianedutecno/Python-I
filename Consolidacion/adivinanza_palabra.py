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

palabras = ['elefante', 'guitarra', 'computadora', 'helado', 'avion']

palabra_secreta = random.choice(palabras)
adivinanza = ""
intentos = 0
max_intentos = 5

print("¡Bienvenido al juego de adivinanza de palabras!")
print("Adivina la palabra secreta. Solo tienes", max_intentos, "intentos.")

while adivinanza != palabra_secreta and intentos < max_intentos:
    adivinanza = input("Ingresa tu adivinanza: ")
    intentos += 1

    if adivinanza == palabra_secreta:
        print("¡Felicitaciones! Adivinaste la palabra secreta en", intentos, "intentos.")
    elif intentos == max_intentos:
        print("Lo siento, no tienes más intentos. La palabra secreta era", palabra_secreta)
    else:
        print("Tu adivinanza es incorrecta. Intenta nuevamente.")


