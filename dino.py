class Dino:
    #cola, dientes, color, size
    #def __init__(self, nombre):                   #init: crea, van los argumentos
       # print("Hola soy un dinosaurio, me llamo", nombre)

#pepito = Dino("pepe")

#agregarle una propiedad color a la clase Dino, y que salude
#diciendo de que color es el dinosaurio

    #def __init__(self, nombre, color):
     #   print("Hola soy un dinosaurio, me llamo", nombre, "y soy de color", color)

#pepito = Dino("pepe", "verde")

#agregarle una propiedad color a la clase Dino, y que salude
#diciendo su nombre y de que color es el dinosaurio
class Dino: 
    def __init__(self, un_nombre="", un_color="verde"):
        self.nombre = un_nombre                 #self es el objeto: pepito
        self.color = un_color
        print("Hola soy un dinosaurio, me llamo", self.nombre, "y soy de color", self.color)

    def cambiar_color(self, un_color):          #metodo es cambiar_color
        self.color = un_color 



pepito = Dino("pepe", "verde")   #Instanciamos o creamos el objeto de tipo DinoAtributos de pepito
print(pepito.nombre)        #Accedemos a la propiedad/Atributo del objeto e imprimimos
pepito.cambiar_color("Lila")         
#pepita = Dino("pepa", "azul")

#agregarle una propiedad color a la clase Dino, y que salude
#diciendo su nombre y de que color es el dinosaurio



