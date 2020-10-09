

#Clase para entender mas a profundidad las abstracciones
#Definicion de la clase
class Lavadora():
        
    def __init__(self):
        pass
    
    def lavar(self):
        self.llenado = llenado
        self.lavado = lavado
        self.centrifugado = centrifugado
        self.enjuaga = enjuaga
        self.seca = seca
                
#Proceso de identidad
        
    def _llenado(self):
        print('')
            
    def _lavado(self):
        print('el ha empezado')
            
    def _centrifugado(self):
        print('el ha comenzado')
           
    def _enjuaga(self):
        print('Esta centrifugando la maquina')
        
    def _seca(self):
        print('Esta secando la maquina')
    
if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()