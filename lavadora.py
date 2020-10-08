

#Clase para entender mas a profundidad las abstracciones
#Definicion de la clase
class Lavadora():
    
    def __init__(self, llenado, lavado, centrifugado, enjuaga, seca):
        self.llenado = llenado
        self.lavado = lavado
        self.centrifugado = centrifugado
        self.enjuaga = enjuaga
        self.seca = seca
        self._microchip_inicio = 'Encender'
        self._microchip_apagado = 'Apagado'
        
#Proceso de identidad
        
    def inicio(self, llenado, lavado, _microchip_inicio = 'Encendido'):
        print('el {}, y {}, comenzaron'.format(llenado, lavado))
        return
    
    def vaciado_agua(self, centrifugado,):
        print('el {}, ha empezado',format(centrifugado))
        return
    
    def finalizacion_lavado(self, seca, _microchip_apagado = 'Apagado'):
        print('el {} ha comenzado'.format(seca))
        return
    
#Objeto

if __name__ == "__main__":
    lavadora = Lavadora('llenando', 'lavado', 'centrifugado', 'enjuagado', 'seca')

    lavadora.inicio(llenado, lavado)
    lavadora.vaciado_agua(centrifugado)
    lavadora.finalizacion_lavado(seca)



    

        