lista_de_listas = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]

for lista in lista_de_listas:
    if lista[0] == 0:
        continue    
    for num in lista:
        if num == 0:
            continue        
        print(num)