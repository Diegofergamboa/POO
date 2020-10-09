

#Clase horno microhondas, va a tener dos funciones, (i) cocinar, (ii) tostar.

class Horno:
    
#iteraciones de las funciones (mètodos)

    def __init__(self):
        pass
    
    def cocinar(self):
        self._cocinar
        self._aumentartemperatura ()
        self._rotareje()
        self._aumentarcalor()
        
    def _cocinar(self):
        print('Comenzando con el proceso de cocinar')
        print('')

    def _aumentartemperatura(self):
        print('Comenzando a aumentar el calor')
    
    def _rotareje(self):
        print('Comenzando la rotaciòn de eje')
    
    def _aumentarcalor(self):
        print('Aumentando calor')
        
#Creaciòn de objetos.
#JHay que tener cuidado con la identaciòn, en python la identaciòn es bastante delicada
    
if __name__ == '__main__':
    horno = Horno()
    horno.cocinar()
    

    
    

