'''
    Modulo de busqueda y ordenacion
    para desarrollar la aplicacion de complejidad algoritmica
    y, ver que algoritmos tenemos a nuestra disposicion
    Es decir intentar buscar algoritmos mas eficientes
'''
###### Busqueda lineal ########

# Ver cada uno de los elemtnso y ver si lo podemos ver en una lista, es decir si existe o no
# EL PEOR CASO = Que despues de 1 millon de iteraciones no lo podamos crear
# Big(O) de este logaritmo

# Se importa libreria para generar valores random los cuales se van a usar en listas

import random

# Se comienza a construir el algoritmo
# La variable match es basicamente la que dice si el objetivo y el elemento coinciden

def busqueda_lineal(objeto, lista):
    match = False
    for elemento in lista:
        if elemento == objetivo:
            match = True
        break
    return match

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')