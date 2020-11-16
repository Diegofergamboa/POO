'''
    Notacion asintotica = NOs va a permitir encuadrar cada uno de los algoritmos que escribamos en una
    de las clases que podamos compararlos  entender como va a crecer
    Asintotico (Hacia donde se va a acercando cuando crece hacia el infinito)
    * No importan las variaciones pequeñas
    * Mejor de los casos (Cunaod en un algoritmo de busqueda se encuentra de primera), promedio, Peor de los casos
    * Big O - La mejor opcion para entender es en el peor de los casos -, lo que importa es nada mas 
    el termino de menor tamaño
'''
'''
    ################ LEY DE LA SUMA ###############
    @@@ La funcion crece en Big O of n
    def f(n):
        for i in range(n):
            print(i)
        for i in range(n):
            print(i)
            
    ############### 0(n) +  0(n) = O (n + n) = 0(2n) = 0(n) ################
    
    ################ LEY DE LA SUMA ############
    @@@ Aqui se ve que ya el crecimiento es mucho mayor, debido principalmente
    a que ya el algoritmo esta creciendo de uan mayor manera es decir de una manera cuadratica
    def f(n):
        for i in range(n):
            print(i)
        for i in range(n*n):
            print(i)
    ############### O(n) + O(n*n) = O(n + n al cuadrado) = O(n al cuadrado)###############
    
    
    ################## LEY DE LA MULTIPLICACION #####################
    
    def f(n):
        for i in range(n):
            for j in range(n):
                print(i, j)
    ################## Esto da un crecimiento cuadratico porque un loop adentro de otro loop #########
    Loop dentro de otro loop es cuadratico
    Loop solito es lineal
    
    ################ RECURSIVIDAD MULTIPLE ###############
    
    def fibonacci(n):
        if n == 0 or n == 1:
           return 1
        return fibonacci(n-1) + fibonacci(n-2) 
        
    Nuestro crecimiento es exponencial en este caos con la funcion de fibonacci
    Si nos damos cuenta aqui esto no escala, es un crecimiento exponencial dependiendo de n
    
    ################ O (2**n) ###################
'''
    
    
       
        