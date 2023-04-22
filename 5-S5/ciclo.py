#ciclos
# ejecutan intrucciones repetitivas hasta que se cumpla una condicion, o se finalice el ciclo o loop

#ciclo for
#for i in data:
#   instrucciones a realizar
frutas = ["Frutilla","Avocado","Manzana"]

for i in frutas:
    print(i)
    
#for i in range(len(data)):
for i in range(1,6):
    print(i)   
    

#conocemos los elementos    
for i in range(len(frutas)):
    print(i)

#conocemos los elementos y la posicion
palabra = "Python"    
for i in range(len(palabra)):
    print(palabra[i])
