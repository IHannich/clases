#crear el archivo que se llame clases y adentro poner los 
#archivos dino.py persona.py

#crear una clase Persona() en el archivo persona.py que tenga como atributos
#nombre, edad y profesion.
#Al instanciar la clase tiene que saludar igual que el dino diciendo sus atributos

class Persona:
    def __init__ (self, un_nombre, una_edad, una_profesion, un_cumple):
        self.nombre = un_nombre             #self.nombre se refiere al objeto en sì. Ya queda en el objeto
        self.edad = una_edad
        self.profesion = una_profesion
        self.cumpleaños = un_cumple
        print("Hola mi nombre es", self.nombre, "tengo", self.edad, "y soy", self.profesion) 
    def cumple1(self):
        self.edad = self.edad + 1
        return self.edad

Yo = Persona("Ingrid", 23, "estudiante", "junio" )  #se crea el objeto "pepito" con los atributos
Yo.cumple1()
Yo.cumple1()
Yo.cumple1()
Yo.cumple1()
Yo.cumple1()
Yo.cumple1()
Yo.cumple1()
Yo.cumple1()
print(edad.Yo)

#Agregar un metodo a la clase persona, que se llame cumpleaños y que aumente la edad de la persona 
# en un año y retorne la edad nueva





