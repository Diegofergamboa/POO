'''
    Toma la estrategia de dividir haciendo el programa mas pequeño hasta que llegamos a la solucion
    se llama binaria porque se divide en dos en cada iteracion, este algoritmo asume que la lista esta
    ordenada.
    * Si se va a usar muchas veces el algoritmo vale la pena intentar ordenarlo, si no no es necesario
      ya que se amortiza el costo que vamos a realizar cada vez.
    * Si la lista no esta ordenada busque lineal, si no es mejor realizarlo de manera binaria
    SIEMPRE SE EMPIEZA A CONTAR DESDE CERO
'''

def busqueda_binaria(lista, comienzo, final, objetivo):
    
    if comienzo > final:
        print('El valor no està en la lista')
        
    medio = (comienzo + final)/2
    
    if lista[medio] < objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio -1, objetivo)

import random 
#Se recomienda escribir esto primero

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

#Funcion sorted ordena la lista

    lista = sorted([random.randint[0, 100] for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
