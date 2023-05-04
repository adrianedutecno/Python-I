import random #importando modulo o libreria random

numero_random = random.randint(0, 10) #numero aleatorio entre 0 y 10, incluye condiciones de borde
# print(numero_random)

print("""Bienvenido al juego de adivinanzas,
      deberas adivinar un numero de 0 a 10 """) 
adivinanza = 11 # incializando variable en un numero diferente al rango de 0 al 10 o alrango del numero aleatorio

contador = 0 #contador para conocer los intentos del usuario

while adivinanza != numero_random: #mientras adivinanza sea diferente al numero_random
    adivinanza = int(input("Ingresa un numero del 0 al 10: ")) #se ingresa el valor en cada iteracion si se cumple la condicion
    contador += 1 
    if adivinanza > numero_random: #evaluando el valor de adivinanza
        print("el numero es mayor al numero a adivinar") 
    elif adivinanza < numero_random:
        print("el numero es menor al numero a adivinar")
    else: 
        print( f"Adivinaste! el numero era {numero_random} en , {contador} intentos")