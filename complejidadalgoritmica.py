'''
    Introduccion a la complejidad algoritmica, el objetivo es generaar abstracciones
    Decomponer un problema en modulos mas especializados
    EL objetivo es ir desarrollnado el pensamiento computacional
    La complejidad algoritmica nos permite medir la efriciencia entre dos algoritmos y predecir el tiempo
    para desarrollar un problema
    COmo analizar billones de paginas en el internet?
    Entender si el algoritmo nos va a decir en cuanto tiempo se va a resolver
    CUanto espacio necesitamos para resolver un problema
    Aqi se va a hablar sobre complejidad temporal y espacial
    Es un funcion T(N) nos va a decir canto tiempo se va a gastar un algoritmo
    El tiempo depende de la ocpacion en el sistema operativo, aparte de eso la calidad del procesador
    @ Cronometrar el tiempo en que corre un algoritmo
    @ Contar los pasos con una medida abstracta
    @ COntar los pasos
    # Conforme el Dataset crece hacia el infinito se deben ir contando los pasos
'''

########Algoritmo de tiempo ###########
# Se debe importar el modulo de Time

import time

# Implementacion recursiva e iterativa

# COn el tiempo en parte no se puede medir exactamente, ese es el problema de medir en tiempo
# Ya que ademas depende de muchos factores


#### 1 implementacion

def factorial(n):
    respuesta = 1
    
    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta

#Factorial recursivo

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

if __name__ ==  '__main__': 
    n = 1000000
    
    comienzo = time.time()
    final = time.time()
    print(final-comienzo)
    
    comienzo = time.time()
    final = time.time()
    print(final - comienzo)
    
    
    
'''
    COn el paso del tiempo nos damos cuenta que en realidad estos se van acercando, lo que nos muestra
    que en realidad la medicion a travès del tiempo no es tan eficiente para medir la eficiencia
    de un algoritmo
'''


