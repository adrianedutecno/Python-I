# Comenzando con el lenguaje Python

""" 
Bloque de comentario
Se puede escribir comentarios en línea y en bloque con 3 comillas dobles o simples al comienzo y final
"""

'''
Comillas secillas para un bloque de comentario
Inicio con estructura basica de python
'''

# metodo para impresion en consola
print("Full Stack Python")
print(2)
print(2+1)

#declaracion de variables
#las variables el nombre es su identificador
cadena = "cadena de caracteres o un String"

#indentacion en python, se realiza con tabulaciones o 1, 2, ...,
if True:
    print("probando condicional")
    print("otra impresion")
    if True:
        print("indentacion en python")    
        
                  
#separacion de bloques de codigo con 2 lineas hacia abajo
print("Separacion de bloques de codigo con 2 lineas hacia abajo")

#tipos de datos
'''
Como sonsultar tipos de datos en python
'''
print(type(5)) #int <class 'int'>
print(type(cadena)) #str <class'str'>
print(type("2"))#str <class'str'>
print(type(True)) #bool <class 'bool'>  
print(type(False)) #bool <class 'bool'>
print(type([])) #list <class 'list'>
print(type(2 + 1j))#complex <class 'complex'>
print(type(None))#None <class 'NoneType'>
print(type(1.5))#float <class 'float'>   