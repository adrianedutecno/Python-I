"""
Requerimos eliminar todas las vocales de la palabra “paralelepípedo”, 
e imprimir en pantalla las consonantes restantes 
y su posición dentro de dicha palabra.
"""

#declarar variable que almacena la palabra “paralelepípedo”
palabra = "paralelepípedo"
consonantes = ""
patron = "aeiíouAEIOU"

#range() convierte cada uno de los elementos en un indice
for i in range(len(palabra)):
    if palabra[i] not in patron:
        consonantes += palabra[i]
        print(f"La letra {palabra[i]} se encuentra en la posición {i}")
        
print(consonantes)
