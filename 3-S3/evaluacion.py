'''
El objetivo de la presente actividad es realizar un cálculo aritmético sencillo, 
haciendo uso de variables, operaciones aritméticas, y de la función print()print(). 
Para ello requerimos importar el módulo mathmath.
ENUNCIADO DEL PROBLEMA:
Requerimos hacer el cálculo de la raíz cuadrada de una variable llamada 
“y que tiene valor 81, utilizando el módulo de la librería math incorporada en Python. 
El resultado debemos asignarlo a una variable que será impresa en pantalla.
'''
import math

#declaracion de variable
y = 81 #asignando valor a la variable

raiz = math.sqrt(y) #acumulando la raíz cuadrada de la variable y en una variable llamada raiz

#impresion en consola de la variable raiz
print(f"La raiz cuadradada de {y} es : {raiz}")


'''
import java.util.Math

 private void main(String[] args){
     int y = 81;
     float raiz = Math.sqrt(y);
     System.out.println("La raiz cuadradada de " + y + " es + " + raiz);
 }
'''