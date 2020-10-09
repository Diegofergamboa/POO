

#Clase para entender mas a profundidad las abstracciones
#Definicion de la clase


class Lavadora:
        
    def __init__(self):
        pass
    
    def lavar(self):
        self._llenado()
        self._lavado()
        self._centrifugado()
        self._enjuaga()
        self._seca()
                
#Proceso de identidad

    def _lavar(self):
        print('Esta comenzando el proceso de lavado')
        
    def _llenado(self):
        print('Llenando la lavadora')
            
    def _lavado(self):
        print('el lavado ha empezado')
            
    def _centrifugado(self):
        print('el centrifugado ha comenzado')
           
    def _enjuaga(self):
        print('La maquina esta enjuagando')
        
    def _seca(self):
        print('Esta secando la maquina')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()