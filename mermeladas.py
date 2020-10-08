#Proceso de produccion de mermeladas

class mermelada():
    
    def __init__(self, lavar, cortar, cocinar, endulzar, maria, enfriar, empacar, temperatura):
        self.lavar = lavar  
        self.cortar = cortar
        self.cocinar = cocinar 
        self.endulzar = endulzar 
        self.maria = maria
        self.enfriar = enfriar 
        self.empacar = empacar
        self._sellado = 'En caliente'
        self.temperatura = temperatura
        
        
    def sellado (self, maria, enfriar, apretar = 'Fuerte', temperatura):
        if temperatura is True:
            apretar = True
        else:
            calentar_hasta30grados():
                
class sabores_mermelada:
    
    def __init__(self, mora, uchuva, durazno):
        self.mora = mora
        self.uchuva = uchuva
        self.durazno = durazno
        self._fresa = fresa
        
    def morauchuva(self, mora, uchuva):
        morauchuva = mora + uchuva
        
    
    
    
        
