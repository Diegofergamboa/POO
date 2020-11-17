'''
    Imaginar que uno es un ladron que quiere entrar pero debes escoger cual de los articulos que vas
    a llevar te va a otorgar el mayor valor posible
    la programacion dinamica sirve para encontrar mejores caminos con respecto a la eficiencia de un programa
'''
def morral(tamano_morral, pesos, valores, n):
    
    if n == 0 or tamano_morral == 0:
        return 0

    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)

    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
                morral(tamano_morral, pesos, valores, n - 1))


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 5
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)