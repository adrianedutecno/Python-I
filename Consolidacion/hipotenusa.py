'''
realizar el calculo de la hipotenusa requiriendo el ingreso del cateto a y cateto b por parte del usuario en consola
'''

import math

print("Cálculo de hipotenusa")
ca = int(input("Ingrese el valor del cateto a del triangulo: "))
cb = int(input("Ingrese el valor del cateto b del triangulo: "))
print("......")

h = math.hypot(ca,cb)
hipotenusa = math.sqrt(ca*ca + cb*cb)
hipo = math.sqrt(ca**2 + cb**2)

print("El resultado de la hipotenusa teniendo el cateto a1 {} y el cateto b1 {} es: {:.3f}".format(ca, cb, h))
print("El resultado de la hipotenusa teniendo el cateto a {} y el cateto b {} es: {:.3f}".format(ca, cb, hipotenusa))
print("El resultado de la hipotenusa teniendo el cateto a {} y el cateto b {} es: {:.3f}".format(ca, cb, hipo))
