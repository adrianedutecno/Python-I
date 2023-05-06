numeros = input('ingrese 3 numeros distintos separados por coma (,) :') 
#"1,2,3".split(',') = [1,2,3]
numeros = [ int(i) for i in numeros.split(',') ] 

def check_length_three(num: list) -> bool: 
    if len(num) == 3: 
        return True 
    else: 
        return False 
    
def matematicas(): 
    suma=sum(numeros) 
    print(f"la suma de los parametros es {suma}") 
    b = numeros[0]-numeros[1]-numeros[2] 
    print (f"la resta del segundo y tercer parametro al primero es {b}") 
    tupla = suma, b 
    print(tupla) 
    
while check_length_three(numeros) == False: 
    numeros = input('Debe ingresar 3 numeros separados por coma (,) :') 
    numeros = [ int(i) for i in numeros.split(',') ] # print("Los numeros ingresadosson:") matematicas()