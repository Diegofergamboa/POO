
class vehiculo():
    
    def __init__(self, kilometros, consumo, sillas, potencia, motor):   
        self.kilometros = kilometros
        self.consumo = consumo
        self.sillas = sillas
        self.potencia = potencia
        self.motor = motor
    
    def addkilometros(self, nuevoskilometros):
        kilometros = self.kilometros + nuevoskilometros
        print('Los kilometros que se aumentaron son {}'.format(kilometros))
        return
    
    def addconsumo(self, motor, consumo):
        print('El tipo de motor {}, consume {} cantidad de combustible'.format(motor, consumo))
        return
    
    def addsillas(self, sillas, sumasillas):
        sillas = self.sillas + sumasillas
        print('El numero de sillas es {}'.format(sillas))
        return
    
    def addpotencia(self, motor, potencia):
        print('La potencia del motor {}, es {}'.format(motor, potencia))
        return 
    
    def addmotor(self, motor):
       print('El tipo de motor es {}'.format(motor))
       return 
  
  
volkswagen = vehiculo(1980, 'alto', 4, 'buena', 'potente')
volkswagen.addkilometros(50)
volkswagen.addconsumo('regular', 'baja')
volkswagen.addsillas(4, 10)

trasmilenio = vehiculo(7600, 'mediano', 56, 'alta', 'v8')

trasmilenio.addpotencia('v8', 'medianamente alta')
  