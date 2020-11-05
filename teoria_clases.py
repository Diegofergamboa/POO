
#Las clases son aquellas que nos permiten realizar representaciones
#de las abstracciones de la realidad en objetos en la programaciòn

#Los objetos son instancias, las clases son el molde


class Persona:
    pass

#
    def __init__(self, nombre):
        self.nombre = nombre
                
        
    def saluda(self, nombre):
        print('')
        print('Mi nombre es {}, hola {}',format(self.nombre, otra_persona.nombre))
        print('')
              
#Uso

if __name__ == "__main__":
    david = Persona('David')
    erika = Persona('Erika')
    david.saluda(erika)
    
